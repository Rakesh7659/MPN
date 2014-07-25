from django.contrib import admin
from ymht.models import *
from .models import Session, SessionMedia, Attendance
from django.core.exceptions import ValidationError

class SessionMediaInline(admin.StackedInline):
    model = SessionMedia
    extra = 1

class AttendanceInline(admin.StackedInline):
    model = Attendance
    extra = 1

class SessionAdmin(admin.ModelAdmin):
	inlines = [
		SessionMediaInline,
		AttendanceInline
	]
admin.site.register(Session, SessionAdmin)
