from django.db.models import F
from .models import Company, CompanyExecutives


def get_companies(limit=50):
    """
    Returns a limited list of companies ordered by companyid.
    """
    return Company.objects.order_by('companyid')[:limit]


def get_executives_by_company_ids(company_ids):
    """
    Returns executive details for selected company IDs.

    This function performs ORM joins using CompanyExecutives.
    """

    return CompanyExecutives.objects.filter(
        companyid__companyid__in=company_ids
    ).values(
        company_id=F('companyid__companyid'),
        company_name=F('companyid__companyname'),
        executive_name=F('contactid__name'),
        designation=F('contactid__designation'),
        linkedin_handler=F('contactid__linkedinhandler')
    )