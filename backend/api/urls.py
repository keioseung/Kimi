from rest_framework.routers import DefaultRouter
from .views import ProblemViewSet, SubmissionViewSet

router = DefaultRouter()
router.register(r'problems', ProblemViewSet)
router.register(r'submissions', SubmissionViewSet)

urlpatterns = router.urls
