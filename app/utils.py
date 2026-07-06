from django.db import DatabaseError
from django.db.models import (
    F,
    Count,
    Sum,
    Case,
    When,
    IntegerField,
    OuterRef,
    Exists,
)
from django.db.models.functions import Coalesce

from .models import (
    Company,
    CompanyExecutives,
    Persons,
    PushOnesignal,
    CompanyFeeds,
    Hottopics,
    NewsArticleArchive,
    PushScheduled
)


def get_companies(limit=50):
    """
    Returns a limited list of companies ordered by companyid.
    """

    # HANDLE INVALID LIMIT VALUES
    if limit is None or limit <= 0:
        raise ValueError("LIMIT MUST BE GREATER THAN ZERO")

    try:
        # FORCE QUERY EXECUTION
        companies = list(
            Company.objects.order_by("companyid")[:limit]
        )

        # EMPTY LIST IS VALID
        return companies

    # HANDLE DATABASE FAILURES
    except DatabaseError as e:
        raise Exception(
            "FAILED TO FETCH COMPANIES FROM DATABASE"
        ) from e


def get_executives_by_company_ids(company_ids):
    """
    Returns executive details for selected company IDs.

    This function performs ORM joins using CompanyExecutives.
    """

    # HANDLE EMPTY COMPANY IDS
    if not company_ids:
        raise ValueError("COMPANY IDS CANNOT BE EMPTY")

    try:
        # FORCE QUERY EXECUTION
        executives = list(
            CompanyExecutives.objects.filter(
                companyid__companyid__in=company_ids
            ).values(
                company_id=F("companyid__companyid"),
                company_name=F("companyid__companyname"),
                executive_name=F("contactid__name"),
                designation=F("contactid__designation"),
                linkedin_handler=F("contactid__linkedinhandler"),
            )
        )

        # EMPTY LIST IS VALID
        return executives

    # HANDLE DATABASE FAILURES
    except DatabaseError as e:
        raise Exception(
            "FAILED TO FETCH EXECUTIVES FROM DATABASE"
        ) from e


def get_users_count_with_push_notifications():
    """
    Returns the count of users with push notifications enabled.
    """

    try:
        result = PushScheduled.objects.filter(
            is_completed=1
        ).aggregate(
            total=Count("person_id", distinct=True)
        )["total"]

        # HANDLE NULL DATABASE RESPONSE
        return result if result is not None else 0

    # HANDLE DATABASE FAILURES
    except DatabaseError as e:
        raise Exception(
            "FAILED TO FETCH PUSH NOTIFICATION USERS COUNT"
        ) from e


def get_users_count_with_scheduled_notifications():
    """
    Returns the count of users with scheduled notifications.
    """

    try:
        result = PushOnesignal.objects.aggregate(
            total=Count("person_id", distinct=True)
        )["total"]

        # HANDLE NULL DATABASE RESPONSE
        return result if result is not None else 0

    # HANDLE DATABASE FAILURES
    except DatabaseError as e:
        raise Exception(
            "FAILED TO FETCH SCHEDULED NOTIFICATION USERS COUNT"
        ) from e


def get_industries_count():
    """
    Returns count of distinct industry hottopics
    linked with company feeds.
    """

    try:
        result = Hottopics.objects.filter(
            category="Industry",
            companyfeeds__isnull=False,
        ).aggregate(
            total=Count("hottopicid", distinct=True)
        )["total"]

        # HANDLE NULL DATABASE RESPONSE
        return result if result is not None else 0

    # HANDLE DATABASE FAILURES
    except DatabaseError as e:
        raise Exception(
            "FAILED TO FETCH INDUSTRIES COUNT"
        ) from e


def get_industry_news_summary():
    """
    Returns industry-wise news summary including:
    - Total news
    - Relevant news
    - Ignored news
    """

    try:
        relevant_articles = NewsArticleArchive.objects.filter(
            articleid=OuterRef("articleid"),
            tag__icontains="relevant",
        )

        ignored_articles = NewsArticleArchive.objects.filter(
            articleid=OuterRef("articleid"),
            tag__icontains="ignored",
        )

        # FORCE QUERY EXECUTION
        summary = list(
            CompanyFeeds.objects.filter(
                hottopicid__category="Industry"
            )
            .annotate(
                is_relevant=Exists(relevant_articles),
                is_ignored=Exists(ignored_articles),
            )
            .values(
                industry=F("hottopicid__hottopicname")
            )
            .annotate(
                # HANDLE NULL TOTAL NEWS VALUES
                TotalNews=Coalesce(
                    Count("articleid", distinct=True),
                    0,
                ),

                # HANDLE NULL RELEVANT NEWS VALUES
                RelevantNews=Coalesce(
                    Sum(
                        Case(
                            When(is_relevant=True, then=1),
                            default=0,
                            output_field=IntegerField(),
                        )
                    ),
                    0,
                ),

                # HANDLE NULL IGNORED NEWS VALUES
                IgnoredNews=Coalesce(
                    Sum(
                        Case(
                            When(is_ignored=True, then=1),
                            default=0,
                            output_field=IntegerField(),
                        )
                    ),
                    0,
                ),
            )
            .order_by("-TotalNews")
        )

        # EMPTY LIST IS VALID
        return summary

    # HANDLE DATABASE FAILURES
    except DatabaseError as e:
        raise Exception(
            "FAILED TO FETCH INDUSTRY NEWS SUMMARY"
        ) from e

