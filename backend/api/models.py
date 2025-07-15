from django.db import models

class Problem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    starter_code = models.TextField()
    test_cases = models.JSONField()  # [{"input": "1 2", "expected": "3"}]

class Submission(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    output = models.TextField()
    passed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
