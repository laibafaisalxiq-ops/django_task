from django.db.models import F, Count, Sum, Case, When, IntegerField, OuterRef, Exists
from .models import (
    Company,
    CompanyExecutives,
    Persons,
    PushOnesignal,
    CompanyFeeds,
    Hottopics,
    NewsArticleArchive,
)


def get_companies(limit=50):
    """
    Returns a limited list of companies ordered by companyid.
    """
    return Company.objects.order_by("companyid")[:limit]


def get_executives_by_company_ids(company_ids):
    """
    Returns executive details for selected company IDs.

    This function performs ORM joins using CompanyExecutives.
    """

    return CompanyExecutives.objects.filter(
        companyid__companyid__in=company_ids
    ).values(
        company_id=F("companyid__companyid"),
        company_name=F("companyid__companyname"),
        executive_name=F("contactid__name"),
        designation=F("contactid__designation"),
        linkedin_handler=F("contactid__linkedinhandler"),
    )


def get_users_count_with_push_notifications():
    """
    Returns the count of users with push notifications enabled.
    """
    return PushOnesignal.objects.filter(is_scheduled=1).aggregate(
        total=Count("person_id", distinct=True)
    )["total"]


def get_users_count_with_scheduled_notifications():
    """
    Returns the count of users with scheduled notifications.
    """
    return PushOnesignal.objects.aggregate(total=Count("person_id", distinct=True))


def get_industries_count():
    """
    Returns count of distinct industry hottopics
    linked with company feeds.
    """

    return Hottopics.objects.filter(
        category="Industry", companyfeeds__isnull=False
    ).aggregate(total=Count("hottopicid", distinct=True))["total"]


def get_industry_news_summary():
    """
    Returns industry-wise news summary including:
    - Total news
    - Relevant news
    - Ignored news
    """

    relevant_articles = NewsArticleArchive.objects.filter(
        articleid=OuterRef("articleid"), tag__icontains="relevant"
    )

    ignored_articles = NewsArticleArchive.objects.filter(
        articleid=OuterRef("articleid"), tag__icontains="ignored"
    )

    return (
        CompanyFeeds.objects.filter(hottopicid__category="Industry")
        .annotate(
            is_relevant=Exists(relevant_articles), is_ignored=Exists(ignored_articles)
        )
        .values(industry=F("hottopicid__hottopicname"))
        .annotate(
            TotalNews=Count("articleid", distinct=True),
            RelevantNews=Sum(
                Case(
                    When(is_relevant=True, then=1),
                    default=0,
                    output_field=IntegerField(),
                )
            ),
            IgnoredNews=Sum(
                Case(
                    When(is_ignored=True, then=1),
                    default=0,
                    output_field=IntegerField(),
                )
            ),
        )
        .order_by("-TotalNews")
    )
