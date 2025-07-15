import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [problems, setProblems] = useState([]);
  const [selected, setSelected] = useState(null);
  const [code, setCode] = useState('');
  const [result, setResult] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/api/problems/').then(res => {
      setProblems(res.data);
    });
  }, []);

  const runCode = () => {
    axios.post(`http://localhost:8000/api/problems/${selected.id}/run_code/`, {
      code
    }).then(res => {
      setResult(res.data);
    });
  };

  return (
    <div>
      <h1>AI 교육 플랫폼</h1>
      <ul>
        {problems.map(p => (
          <li key={p.id} onClick={() => {
            setSelected(p);
            setCode(p.starter_code);
          }}>
            {p.title}
          </li>
        ))}
      </ul>

      {selected && (
        <div>
          <h2>{selected.title}</h2>
          <p>{selected.description}</p>
          <textarea
            rows={10}
            cols={50}
            value={code}
            onChange={e => setCode(e.target.value)}
          />
          <br />
          <button onClick={runCode}>실행</button>
          {result && (
            <div>
              <h3>결과</h3>
              <pre>{result.output}</pre>
              <p style={{ color: result.passed ? 'green' : 'red' }}>
                {result.passed ? '통과!' : '실패'}
              </p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
