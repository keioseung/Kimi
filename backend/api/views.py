from rest_framework import viewsets
from .models import Problem, Submission
from .serializers import ProblemSerializer, SubmissionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
import subprocess
import json

class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    @action(detail=True, methods=['post'])
    def run_code(self, request, pk=None):
        problem = self.get_object()
        code = request.data.get('code')
        
        # 간단한 실행 (보안 강화 필요)
        try:
            result = subprocess.run(
                ['python3', '-c', code],
                capture_output=True,
                text=True,
                timeout=3
            )
            output = result.stdout.strip()
            passed = all(
                output == case['expected']
                for case in problem.test_cases
            )
            Submission.objects.create(
                problem=problem,
                code=code,
                output=output,
                passed=passed
            )
            return Response({'output': output, 'passed': passed})
        except Exception as e:
            return Response({'error': str(e)}, status=400)

class SubmissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
