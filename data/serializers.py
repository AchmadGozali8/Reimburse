from django.contrib.auth.models import User
from .models import Reimbursement

from rest_framework.serializers import HyperlinkedModelSerializer


class UsersSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'last_login')


class ReimbursementSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Reimbursement
        exclude = ('deleted', 'updated_at', 'deleted_at')
