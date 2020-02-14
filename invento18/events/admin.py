from django.contrib import admin
from .models import Event, Event_register, Ambassador
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', '_type', 'fee','imageurl','posterurl','short_desc','long_desc', 'prize', 'day')
    list_filter = ('category', '_type', 'fee', 'prize')

@admin.register(Event_register)
class Event_registerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'referal_code','event')
    list_filter = ('referal_code', 'event')

@admin.register(Ambassador)
class Ambassador_registerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phone','college','department', 'referal_code')
