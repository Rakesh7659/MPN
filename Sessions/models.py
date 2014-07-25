from django.db import models
from django.contrib.auth.models import User
from ymht.models import Membership


def session_content_file_name(instance, filename):
    return '/'.join(['session', instance.reported_by.user.username, filename])

def session_media_content_file_name(instance, filename):
    return '/'.join(['session_media', instance.session.reported_by.user.username, filename])


class NewSession(models.Model):
	EVENT_CHOICES = ((1, 'General Session'), (2, 'Special Session'), (3, 'Global Event'), (4, 'Local Event'))
	AGE_GROUP_CHOICES = ((1, '13 to 16'), (2, '17 to 21'), (3, '13 to 21'), (4, '21 to 30'))

	name = models.CharField(max_length=25)
	description = models.TextField(blank=True, null=True)
	event_type = models.IntegerField(choices=EVENT_CHOICES, default=1)
	start_date = models.DateField()
	start_date = models.DateField()
	start_time = models.TimeField()
	end_date = models.DateField()
	end_time = models.TimeField()
	location = models.CharField(max_length=25)
	_13_to_16_years = models.BooleanField(blank=True, null=False)
	_17_to_21_years = models.BooleanField(blank=True, null=False)

	
	def __unicode__(self):
		return '%s' % (self.name)


	#def __unicode__(self):
	#	return '%s, %s, %s: %s, %s, %s, %s, %s, %s' % (self.name, self.description, dict(EVENT_CHOICES).get(self.event_type), self.start_date, self.start_time, self.end_date, self.end_time, self.location, self._13_to_16_years, self._17_to_21_years)

	class Meta:
   		verbose_name_plural = 'Create New Session'

class GenerateReport(models.Model):
	CATEGORY_CHOICES = ((1, 'Photo'),
                        (2, 'Video'),
                        (3, 'Other'))
  	
  	session = models.ManyToManyField(NewSession, blank=True, null=True)
  	category = models.IntegerField(choices=CATEGORY_CHOICES)
  	attachment = models.FileField(upload_to=session_media_content_file_name, blank=True, null=True)

  	def __unicode__(self):
  		return '%s' % (self.session)

# Create your models here.
