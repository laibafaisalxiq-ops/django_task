# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Company(models.Model):
    companyid = models.AutoField(
        db_column="CompanyId", primary_key=True
    )  # Field name made lowercase.
    companyname = models.CharField(
        db_column="CompanyName", max_length=250
    )  # Field name made lowercase.
    twittersearch = models.CharField(
        db_column="TwitterSearch", max_length=200, blank=True, null=True
    )  # Field name made lowercase.
    twitterhandler = models.CharField(
        db_column="TwitterHandler", max_length=45, blank=True, null=True
    )  # Field name made lowercase.
    description = models.CharField(
        db_column="Description", max_length=10000, blank=True, null=True
    )  # Field name made lowercase.
    logo = models.CharField(max_length=45, blank=True, null=True)
    linkedinhandler = models.CharField(
        db_column="LinkedInHandler", max_length=250, blank=True, null=True
    )  # Field name made lowercase.
    ticketsymbol = models.CharField(
        db_column="TicketSymbol", max_length=45, blank=True, null=True
    )  # Field name made lowercase.
    industry = models.CharField(
        db_column="Industry", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    stockexchange = models.CharField(
        db_column="StockExchange", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    website = models.CharField(
        db_column="WebSite", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    address = models.CharField(
        db_column="Address", max_length=500, blank=True, null=True
    )  # Field name made lowercase.
    sector = models.CharField(
        db_column="Sector", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    reviewflag = models.IntegerField(
        db_column="ReviewFlag", blank=True, null=True
    )  # Field name made lowercase.
    companyimage = models.TextField(
        db_column="CompanyImage", blank=True, null=True
    )  # Field name made lowercase.
    twitterreviewflag = models.IntegerField(
        db_column="TwitterReviewFlag", blank=True, null=True
    )  # Field name made lowercase.
    linkedinreviewflag = models.IntegerField(
        db_column="LinkedinReviewFlag", blank=True, null=True
    )  # Field name made lowercase.
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
        db_table = "company"


class CompanyExecutives(models.Model):
    contactid = models.ForeignKey(
        "Persons", models.DO_NOTHING, db_column="ContactId"
    )  # Field name made lowercase.
    companyid = models.ForeignKey(
        Company, models.DO_NOTHING, db_column="CompanyId"
    )  # Field name made lowercase.
    type = models.CharField(max_length=20, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "company_executives"
        unique_together = (("companyid", "contactid"),)


class Persons(models.Model):
    contactid = models.AutoField(
        db_column="ContactId", primary_key=True
    )  # Field name made lowercase.
    name = models.CharField(
        db_column="Name", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    designation = models.CharField(
        db_column="Designation", max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    twitterhandler = models.CharField(
        db_column="TwitterHandler", max_length=45, blank=True, null=True
    )  # Field name made lowercase.
    linkedinhandler = models.CharField(
        db_column="LinkedInHandler", max_length=45, blank=True, null=True
    )  # Field name made lowercase.
    biography = models.CharField(max_length=5000, blank=True, null=True)
    age = models.IntegerField(
        db_column="Age", blank=True, null=True
    )  # Field name made lowercase.
    linkedinid = models.CharField(
        db_column="LinkedInId", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    source = models.CharField(
        db_column="Source", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    followers = models.IntegerField(
        db_column="Followers", blank=True, null=True
    )  # Field name made lowercase.
    following = models.IntegerField(
        db_column="Following", blank=True, null=True
    )  # Field name made lowercase.
    tweets = models.IntegerField(
        db_column="Tweets", blank=True, null=True
    )  # Field name made lowercase.
    twitterid = models.BigIntegerField(
        db_column="TwitterId", blank=True, null=True
    )  # Field name made lowercase.
    tweetstatus = models.IntegerField(
        db_column="TweetStatus", blank=True, null=True
    )  # Field name made lowercase.
    positiondetails = models.CharField(
        db_column="PositionDetails", max_length=5000, blank=True, null=True
    )  # Field name made lowercase.
    reviewflag = models.IntegerField(
        db_column="ReviewFlag", blank=True, null=True
    )  # Field name made lowercase.
    image = models.CharField(
        db_column="Image", max_length=1000, blank=True, null=True
    )  # Field name made lowercase.
    rank = models.IntegerField(
        db_column="Rank", blank=True, null=True
    )  # Field name made lowercase.
    industry = models.CharField(
        db_column="Industry", max_length=200, blank=True, null=True
    )  # Field name made lowercase.
    location = models.CharField(
        db_column="Location", max_length=200, blank=True, null=True
    )  # Field name made lowercase.
    connections = models.CharField(
        db_column="Connections", max_length=10, blank=True, null=True
    )  # Field name made lowercase.
    headline = models.CharField(
        db_column="Headline", max_length=1000, blank=True, null=True
    )  # Field name made lowercase.
    summary = models.CharField(
        db_column="Summary", max_length=4000, blank=True, null=True
    )  # Field name made lowercase.
    speciality = models.CharField(
        db_column="Speciality", max_length=4000, blank=True, null=True
    )  # Field name made lowercase.
    company = models.CharField(
        db_column="Company", max_length=200, blank=True, null=True
    )  # Field name made lowercase.
    imageupload = models.CharField(
        db_column="Imageupload", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    imagepath = models.CharField(
        db_column="Imagepath", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    # personality_archetype = models.ForeignKey('ArchetypeDetails', models.DO_NOTHING, db_column='personality_archetype', blank=True, null=True)
    review_status = models.CharField(max_length=20, blank=True, null=True)
    degree = models.IntegerField(blank=True, null=True)
    personality_type = models.CharField(max_length=20, blank=True, null=True)
    review = models.IntegerField(blank=True, null=True)
    url_action = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "persons"


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CompanyFeeds(models.Model):
    companyid = models.ForeignKey(
        "Company", models.DO_NOTHING, db_column="companyid", blank=True, null=True
    )
    articleid = models.ForeignKey(
        "Articles", models.DO_NOTHING, db_column="articleid", blank=True, null=True
    )
    personid = models.ForeignKey(
        "Persons", models.DO_NOTHING, db_column="personid", blank=True, null=True
    )
    # twitterid = models.ForeignKey('TwitterUpdate', models.DO_NOTHING, db_column='twitterid', blank=True, null=True)
    # linkedinid = models.ForeignKey('LinkedinUpdate', models.DO_NOTHING, db_column='linkedinid', blank=True, null=True)
    # sourceid = models.ForeignKey('ArticleSource', models.DO_NOTHING, db_column='sourceid', blank=True, null=True)
    publishdate = models.DateTimeField(blank=True, null=True)
    hottopicid = models.ForeignKey(
        "Hottopics", models.DO_NOTHING, db_column="hottopicid", blank=True, null=True
    )
    content = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=3, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    # alertid = models.ForeignKey('Alerts', models.DO_NOTHING, db_column='alertid', blank=True, null=True)
    # alertarticleid = models.ForeignKey('ArticleAlert', models.DO_NOTHING, db_column='alertarticleid', blank=True, null=True)
    priority = models.FloatField(blank=True, null=True)
    classified = models.IntegerField(blank=True, null=True)
    processtime = models.DateTimeField()
    subtype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "company_feeds"


class PushOnesignal(models.Model):
    notification_clicks = models.IntegerField(blank=True, null=True)
    sent_push_count = models.IntegerField(blank=True, null=True)
    delivery_success_count = models.IntegerField(blank=True, null=True)
    person_id = models.IntegerField(blank=True, null=True)
    app_id = models.CharField(max_length=255, blank=True, null=True)
    notification_id = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    heading = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    platform_delivery = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    push_data = models.TextField(blank=True, null=True)
    canceled = models.IntegerField(blank=True, null=True)
    queued_at = models.DateTimeField()
    send_after = models.DateTimeField()
    completed_at = models.DateTimeField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    article_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "push_onesignal"


class Hottopics(models.Model):
    hottopicid = models.AutoField(
        db_column="HotTopicId", primary_key=True
    )  # Field name made lowercase.
    hottopicname = models.CharField(
        db_column="HotTopicName", max_length=45
    )  # Field name made lowercase.
    category = models.CharField(
        db_column="Category", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    image = models.TextField(
        db_column="Image", blank=True, null=True
    )  # Field name made lowercase.
    hottopicimage = models.TextField(blank=True, null=True)
    dbsid = models.IntegerField(blank=True, null=True)
    for_digest = models.IntegerField(blank=True, null=True)
    dbid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "hottopics"


class NewsArticleArchive(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    buid = models.IntegerField(blank=True, null=True)
    articleid = models.IntegerField(blank=True, null=True)
    archive = models.IntegerField(blank=True, null=True)
    tag = models.CharField(max_length=20, blank=True, null=True)
    # alertid1 = models.IntegerField(blank=True, null=True)
    # alertid2 = models.IntegerField(blank=True, null=True)
    # alertid3 = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    domain = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    palertid1 = models.IntegerField(blank=True, null=True)
    palertid2 = models.IntegerField(blank=True, null=True)
    insertion_date = models.DateTimeField()
    publishdate = models.DateTimeField()
    news_archive_history_id = models.IntegerField(blank=True, null=True)
    rank = models.FloatField(blank=True, null=True)
    log = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "news_article_archive"
        unique_together = (("companyid", "articleid"),)


class Articles(models.Model):
    articleid = models.AutoField(
        db_column="ArticleId", primary_key=True
    )  # Field name made lowercase.
    article = models.TextField(
        db_column="Article", blank=True, null=True
    )  # Field name made lowercase.
    likes = models.IntegerField(
        db_column="Likes", blank=True, null=True
    )  # Field name made lowercase.
    shared = models.IntegerField(
        db_column="Shared", blank=True, null=True
    )  # Field name made lowercase.
    source = models.CharField(
        db_column="Source", max_length=45, blank=True, null=True
    )  # Field name made lowercase.
    link = models.CharField(max_length=1500, blank=True, null=True)
    title = models.CharField(
        db_column="Title", max_length=1000, blank=True, null=True
    )  # Field name made lowercase.
    status = models.SmallIntegerField(
        db_column="Status", blank=True, null=True
    )  # Field name made lowercase.
    domain = models.CharField(
        db_column="Domain", max_length=40, blank=True, null=True
    )  # Field name made lowercase.
    favicon = models.CharField(
        db_column="Favicon", max_length=400, blank=True, null=True
    )  # Field name made lowercase.
    publishdate = models.DateTimeField(
        db_column="PublishDate"
    )  # Field name made lowercase.
    currentdate = models.DateTimeField(
        db_column="CurrentDate"
    )  # Field name made lowercase.
    description = models.CharField(
        db_column="Description", max_length=5000, blank=True, null=True
    )  # Field name made lowercase.
    imageurl = models.CharField(
        db_column="ImageURL", max_length=1000, blank=True, null=True
    )  # Field name made lowercase.
    error = models.CharField(max_length=1500, blank=True, null=True)
    author = models.CharField(
        db_column="Author", max_length=150, blank=True, null=True
    )  # Field name made lowercase.
    errorcount = models.IntegerField(
        db_column="errorCount", blank=True, null=True
    )  # Field name made lowercase.
    views = models.IntegerField(
        db_column="Views", blank=True, null=True
    )  # Field name made lowercase.
    originalurl = models.CharField(
        db_column="OriginalUrl", max_length=1500, blank=True, null=True
    )  # Field name made lowercase.
    save = models.IntegerField(
        db_column="Save", blank=True, null=True
    )  # Field name made lowercase.
    count = models.IntegerField(
        db_column="Count", blank=True, null=True
    )  # Field name made lowercase.
    video = models.CharField(max_length=4000, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    hash = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "articles"
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PushScheduled(models.Model):
    #article = models.ForeignKey('Articles', models.DO_NOTHING)
    #user = models.ForeignKey('User', models.DO_NOTHING)
    #dbbu = models.ForeignKey('DailyBulletinBu', models.DO_NOTHING, blank=True, null=True)
    #company = models.ForeignKey('Company', models.DO_NOTHING, blank=True, null=True)
    is_completed = models.IntegerField()
    is_read = models.IntegerField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    #digest_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'push_scheduled'
