import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    CompanySerializer,
    ExecutiveSerializer,
)

from .utils import (
    get_companies,
    get_executives_by_company_ids,
    get_users_count_with_push_notifications,
    get_users_count_with_scheduled_notifications,
    get_industries_count,
    get_industry_news_summary,
)

logger = logging.getLogger("app")


@api_view(["GET"])
def company_list(request):
    """
    API endpoint to return list of companies.
    """

    logger.info("Company list API called")

    try:
        companies = get_companies(limit=50)

        # CHANGED: UTILS RETURNS PYTHON LIST
        logger.info(
            "Successfully fetched %s companies",
            len(companies),
        )

        serializer = CompanySerializer(
            companies,
            many=True,
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        logger.exception(
            "Error fetching companies: %s",
            str(e),
        )

        return Response(
            {
                "error": "Failed to fetch companies",
                "details": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def executive_list(request):
    """
    API endpoint to return executives
    for selected companies.
    """

    logger.info("Executive list API called")

    try:
        company_ids = [190, 199, 225, 296]

        logger.info(
            "Fetching executives for company IDs: %s",
            company_ids,
        )

        executives = get_executives_by_company_ids(
            company_ids
        )

        # CHANGED: UTILS RETURNS PYTHON LIST
        logger.info(
            "Successfully fetched %s executives",
            len(executives),
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
        logger.exception(
            "Error fetching executives: %s",
            str(e),
        )

        return Response(
            {
                "error": "Failed to fetch executives",
                "details": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def count_users_with_push_notifications(request):
    """
    API endpoint to count users
    with push notifications enabled.
    """

    logger.info(
        "Count users with push notifications API called"
    )

    try:
        count = (
            get_users_count_with_push_notifications()
        )

        return Response(
            {"count": count},
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        logger.exception(
            "Error counting users with "
            "push notifications: %s",
            str(e),
        )

        return Response(
            {
                "error":
                "Failed to count users "
                "with push notifications",
                "details": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def users_count_with_scheduled_notifications(request):
    """
    API endpoint to count users
    with scheduled notifications.
    """

    logger.info(
        "Count users with scheduled "
        "notifications API called"
    )

    try:
        count = (
            get_users_count_with_scheduled_notifications()
        )

        return Response(
            {"count": count},
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        logger.exception(
            "Error counting users with "
            "scheduled notifications: %s",
            str(e),
        )

        return Response(
            {
                "error":
                "Failed to count users "
                "with scheduled notifications",
                "details": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def industries_count(request):
    """
    API endpoint to count total
    number of industries in xiQ.
    """

    logger.info(
        "Count total number of industries "
        "in xiQ API called"
    )

    try:
        industry_count = get_industries_count()

        return Response(
            {"count": industry_count},
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        logger.exception(
            "Error counting industries: %s",
            str(e),
        )

        return Response(
            {
                "error": "Failed to count industries",
                "details": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def industry_news_summary(request):
    """
    API endpoint to return
    industry-wise news summary.
    """

    logger.info(
        "Industry news summary API called"
    )

    try:
        data = get_industry_news_summary()

        return Response(
            data,
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        logger.exception(
            "Error fetching industry "
            "news summary: %s",
            str(e),
        )

        return Response(
            {
                "error":
                "Failed to fetch industry "
                "news summary",
                "details": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

