from django.urls import path

from .views import company_list, executive_list, count_users_with_push_notifications
from .views import (
    users_count_with_scheduled_notifications,
    industries_count,
    industry_news_summary,
)

urlpatterns = [
    path(
        "",
        company_list,
        name="companies",  # internal routing
    ),
    path("executives", executive_list, name="executives"),
    path(
        "users_count_with_push_notifications",
        count_users_with_push_notifications,
        name="users_count_with_push_notifications",
    ),
    path(
        "users_count_with_scheduled_notifications",
        users_count_with_scheduled_notifications,
        name="users_count_with_scheduled_notifications",
    ),
    path("industries_count", industries_count, name="industries_count"),
    path("industry_news_summary", industry_news_summary, name="industry_news_summary"),
]
