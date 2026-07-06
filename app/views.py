import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import CompanySerializer, ExecutiveSerializer
from .utils import (
    get_companies,
    get_executives_by_company_ids,
    get_users_count_with_push_notifications,
)
from .utils import (
    get_users_count_with_scheduled_notifications,
    get_industries_count,
    get_industry_news_summary,
)

logger = logging.getLogger("app")


```python id="i0mj67"
@api_view(["GET"])
def company_list(request):
    """
    API endpoint to return list of companies (limited result set).
    """

    logger.info("Company list API called")

    try:
        companies = get_companies(limit=50)

        # Handle actual null response only
        if companies is None:
            logger.error("Companies queryset returned None")

            return Response(
                {"error": "No companies data available"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        logger.info(
            "Successfully fetched %s companies",
            companies.count(),
        )

        serializer = CompanySerializer(companies, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        logger.exception(f"Error fetching companies: {str(e)}")

        return Response(
            {
                "error": "Failed to fetch companies",
                "details": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
```

    """
    API endpoint to return list of companies (limited result set).
    """

    logger.info("Company list API called")

    try:
        companies = get_companies(limit=50)

        # Handle null queryset/object if companies is None
        if not companies:
            logger.error("Companies queryset returned None")
            return Response(
                {"error": "No companies data available"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        logger.info(f"Successfully fetched {len(companies)} companies")

        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        logger.exception(f"Error fetching companies: {str(e)}")

        return Response(
            {"error": "Failed to fetch companies", "details": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


```python id="d32rmf"
@api_view(["GET"])
def executive_list(request):
    """
    API endpoint to return executives for selected companies.
    """

    logger.info("Executive list API called")

    try:
        company_ids = [190, 199, 225, 296]

        logger.info(
            f"Fetching executives for company IDs: {company_ids}"
        )

        executives = get_executives_by_company_ids(company_ids)

        # Handle actual null response only
        if executives is None:
            logger.error("Executives queryset returned None")

            return Response(
                {"error": "No executives data available"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        logger.info(
            "Successfully fetched %s executives",
            executives.count(),
        )

        serializer = ExecutiveSerializer(
            executives,
            many=True,
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        logger.exception(f"Error fetching executives: {str(e)}")

        return Response(
            {
                "error": "Failed to fetch executives",
                "details": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
```

    """
    API endpoint to return executives for selected companies.
    """

    logger.info("Executive list API called")

    try:
        company_ids = [190, 199, 225, 296]

        logger.info(f"Fetching executives for company IDs: {company_ids}")

        executives = get_executives_by_company_ids(company_ids)

        # Handle null queryset/object if executives is None
        if not executives:
            logger.error("Executives queryset returned None")
            return Response(
                {"error": "No executives data available"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        logger.info(f"Successfully fetched {len(executives)} executives")

        serializer = ExecutiveSerializer(executives, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        logger.exception(f"Error fetching executives: {str(e)}")

        return Response(
            {"error": "Failed to fetch executives", "details": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def count_users_with_push_notifications(request):
    """
    API endpoint to count users with push notifications enabled.
    """

    logger.info("Count users with push notifications API called")

    try:
        count = get_users_count_with_push_notifications()

        if count is None:
            logger.error("Push notifications count returned None")
            return Response(
                {"error": "Invalid push notification count"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        logger.info(
            f"Successfully counted {count} users with push notifications enabled"
        )

        return Response({"count": count}, status=status.HTTP_200_OK)

    except Exception as e:
        logger.exception(f"Error counting users with push notifications: {str(e)}")

        return Response(
            {
                "error": "Failed to count users with push notifications",
                "details": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def users_count_with_scheduled_notifications(request):
    """
    API endpoint to count users with scheduled notifications.
    """

    logger.info("Count users with scheduled notifications API called")

    try:
        count = get_users_count_with_scheduled_notifications()

        if count is None:
            logger.error("Scheduled notifications count returned None")
            return Response(
                {"error": "Invalid scheduled notifications count"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        logger.info(f"Successfully counted {count} users with scheduled notifications")

        return Response({"count": count}, status=status.HTTP_200_OK)

    except Exception as e:
        logger.exception(f"Error counting users with scheduled notifications: {str(e)}")

        return Response(
            {
                "error": "Failed to count users with scheduled notifications",
                "details": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def industries_count(request):
    """
    API endpoint to count total number of industries in xiQ.
    """

    logger.info("Count total number of industries in xiQ API called")

    try:
        # Assuming you have a function to get the count of industries
        industry_count = get_industries_count()

        if industry_count is None:
            logger.error("Industry count returned None")
            return Response(
                {"error": "Invalid industry count"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        logger.info(f"Successfully counted industries: {industry_count}")

        return Response({"count": industry_count}, status=status.HTTP_200_OK)

    except Exception as e:
        logger.exception(f"Error counting industries: {str(e)}")

        return Response(
            {"error": "Failed to count industries", "details": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def industry_news_summary(request):
    """
    API endpoint to return industry-wise news summary.
    """

    logger.info("Industry news summary API called")

    try:
        data = get_industry_news_summary()

        if data is None:
            logger.error("Industry news summary returned None")
            return Response(
                {"error": "No industry news summary available"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        logger.info("Successfully fetched industry news summary")

        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        logger.exception(f"Error fetching industry news summary: {str(e)}")

        return Response(
            {"error": "Failed to fetch industry news summary", "details": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
