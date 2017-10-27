from rest_framework.routers import DefaultRouter
from .api import UserViewSet, ReimbursementViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'reimburse', ReimbursementViewSet)
