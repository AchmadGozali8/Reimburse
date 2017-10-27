from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .models import Reimbursement
from .serializers import UsersSerializer, ReimbursementSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class ReimbursementViewSet(ModelViewSet):
    queryset = Reimbursement.objects.all()
    serializer_class = ReimbursementSerializer
