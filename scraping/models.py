from django.db import models
from django.utils import timezone

# Create your models here.
''' There will be 2 models present. 1 for the posts themselves, and another for the responses. '''
class RedditPostData(models.Model):
    title = models.CharField(max_length=300)        # Somewhat arbitrary limit, but RES puts the limit at 300 characters.
    score = models.IntegerField()
    post_id = models.CharField(max_length=20)       # Not sure of the actual max, but it is likely lower (looks like something 2_6 = 9 total characters?)
    url = models.URLField(max_length=2000)          # 2083 is the exact max in IE, it differs from service to service, but 2000 is safe here.
    num_comments = models.IntegerField()
    date = models.DateTimeField()
    post_body = models.CharField(max_length=40000)  # Reddit limits self posts to 40000 characters. 

class RedditReplyData(models.Model):
    score = models.IntegerField()
    post_id = models.IntegerField()
    parent_id = models.IntegerField()
    post_body = models.CharField(max_length=40000)