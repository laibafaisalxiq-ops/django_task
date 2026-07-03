from rest_framework import serializers

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company

        fields = ["companyname", "twitterhandler", "website", "country"]


class ExecutiveSerializer(serializers.Serializer):

    company_id = serializers.IntegerField()

    company_name = serializers.CharField()

    executive_name = serializers.CharField()

    designation = serializers.CharField()

    linkedin_handler = serializers.CharField()
