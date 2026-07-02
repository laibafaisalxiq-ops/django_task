from django.urls import path

from .views import company_list,executive_list


urlpatterns = [
    path(
        '',
        company_list,
        name='companies',#internal routing
    ),
    path(
        'executives',
        executive_list,
        name='executives'
    )

]