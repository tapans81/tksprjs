from rest_framework import serializers
from .models import Person,Customer
from django.conf import settings
from .models import Person,Customer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = '__all__'

class CustomerSerializer1(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        url = serializers.HyperlinkedIdentityField(view_name="polls:customer-detail")
        fields = '__all__'
