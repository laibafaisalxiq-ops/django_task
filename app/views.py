import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import CompanySerializer, ExecutiveSerializer
from .utils import get_companies, get_executives_by_company_ids

logger = logging.getLogger('app')


@api_view(['GET'])
def company_list(request):
    """
    API endpoint to return list of companies (limited result set).
    """

    logger.info("Company list API called")

    try:
        companies = get_companies(limit=50)

        logger.info(f"Successfully fetched {len(companies)} companies")

        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        logger.exception(f"Error fetching companies: {str(e)}")

        return Response(
            {
                "error": "Failed to fetch companies",
                "details": str(e)
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def executive_list(request):
    """
    API endpoint to return executives for selected companies.
    """

    logger.info("Executive list API called")

    try:
        company_ids = [190, 199, 225, 296]

        logger.info(f"Fetching executives for company IDs: {company_ids}")

        executives = get_executives_by_company_ids(company_ids)

        logger.info(f"Successfully fetched {len(executives)} executives")

        serializer = ExecutiveSerializer(executives, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        logger.exception(f"Error fetching executives: {str(e)}")

        return Response(
            {
                "error": "Failed to fetch executives",
                "details": str(e)
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )