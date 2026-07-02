import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CompanySerializer, ExecutiveSerializer
from .utils import get_companies, get_executives_by_company_ids

logger = logging.getLogger('app')


@api_view(['GET'])
def company_list(request):
    """
    API endpoint to return list of companies (limited result set).
    """

    logger.info("Company list API called")

    companies = get_companies(limit=50)

    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def executive_list(request):
    """
    API endpoint to return executives for selected companies.
    """

    logger.info("Executive list API called")

    company_ids = [190, 199, 225, 296]

    executives = get_executives_by_company_ids(company_ids)

    serializer = ExecutiveSerializer(executives, many=True)
    return Response(serializer.data)