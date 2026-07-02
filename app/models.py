# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Company(models.Model):
    companyid = models.AutoField(db_column='CompanyId', primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=250)  # Field name made lowercase.
    twittersearch = models.CharField(db_column='TwitterSearch', max_length=200, blank=True, null=True)  # Field name made lowercase.
    twitterhandler = models.CharField(db_column='TwitterHandler', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    logo = models.CharField(max_length=45, blank=True, null=True)
    linkedinhandler = models.CharField(db_column='LinkedInHandler', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ticketsymbol = models.CharField(db_column='TicketSymbol', max_length=45, blank=True, null=True)  # Field name made lowercase.
    industry = models.CharField(db_column='Industry', max_length=300, blank=True, null=True)  # Field name made lowercase.
    stockexchange = models.CharField(db_column='StockExchange', max_length=50, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='WebSite', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reviewflag = models.IntegerField(db_column='ReviewFlag', blank=True, null=True)  # Field name made lowercase.
    companyimage = models.TextField(db_column='CompanyImage', blank=True, null=True)  # Field name made lowercase.
    twitterreviewflag = models.IntegerField(db_column='TwitterReviewFlag', blank=True, null=True)  # Field name made lowercase.
    linkedinreviewflag = models.IntegerField(db_column='LinkedinReviewFlag', blank=True, null=True)  # Field name made lowercase.
    hottopicid = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    auditentry = models.DateTimeField(blank=True, null=True)
    launchpadimage = models.CharField(max_length=1000, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    duns_id = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=25, blank=True, null=True)
    latitude = models.CharField(max_length=25, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    domain = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class CompanyExecutives(models.Model):
    contactid = models.ForeignKey('Persons', models.DO_NOTHING, db_column='ContactId')  # Field name made lowercase.
    companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    type = models.CharField(max_length=20, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_executives'
        unique_together = (('companyid', 'contactid'),)


class Persons(models.Model):
    contactid = models.AutoField(db_column='ContactId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=300, blank=True, null=True)  # Field name made lowercase.
    twitterhandler = models.CharField(db_column='TwitterHandler', max_length=45, blank=True, null=True)  # Field name made lowercase.
    linkedinhandler = models.CharField(db_column='LinkedInHandler', max_length=45, blank=True, null=True)  # Field name made lowercase.
    biography = models.CharField(max_length=5000, blank=True, null=True)
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    linkedinid = models.CharField(db_column='LinkedInId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=20, blank=True, null=True)  # Field name made lowercase.
    followers = models.IntegerField(db_column='Followers', blank=True, null=True)  # Field name made lowercase.
    following = models.IntegerField(db_column='Following', blank=True, null=True)  # Field name made lowercase.
    tweets = models.IntegerField(db_column='Tweets', blank=True, null=True)  # Field name made lowercase.
    twitterid = models.BigIntegerField(db_column='TwitterId', blank=True, null=True)  # Field name made lowercase.
    tweetstatus = models.IntegerField(db_column='TweetStatus', blank=True, null=True)  # Field name made lowercase.
    positiondetails = models.CharField(db_column='PositionDetails', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    reviewflag = models.IntegerField(db_column='ReviewFlag', blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    industry = models.CharField(db_column='Industry', max_length=200, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=200, blank=True, null=True)  # Field name made lowercase.
    connections = models.CharField(db_column='Connections', max_length=10, blank=True, null=True)  # Field name made lowercase.
    headline = models.CharField(db_column='Headline', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    summary = models.CharField(db_column='Summary', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    speciality = models.CharField(db_column='Speciality', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=200, blank=True, null=True)  # Field name made lowercase.
    imageupload = models.CharField(db_column='Imageupload', max_length=100, blank=True, null=True)  # Field name made lowercase.
    imagepath = models.CharField(db_column='Imagepath', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    #personality_archetype = models.ForeignKey('ArchetypeDetails', models.DO_NOTHING, db_column='personality_archetype', blank=True, null=True)
    review_status = models.CharField(max_length=20, blank=True, null=True)
    degree = models.IntegerField(blank=True, null=True)
    personality_type = models.CharField(max_length=20, blank=True, null=True)
    review = models.IntegerField(blank=True, null=True)
    url_action = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons'
