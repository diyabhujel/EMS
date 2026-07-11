from django.contrib import admin
from .models import Event,Bookings,ExpiredEvent

# Register your models here.
class EventAdmin(admin.ModelAdmin):
  list_display = ['name','seats','dnt','venue']
admin.site.register(Event)
admin.site.register(Bookings)

from django.utils import timezone
class ExpiredEventAdmin(admin.ModelAdmin):
  def get_queryset(self, request):
    return super().get_queryset(request).filter(dnt_lt=timezone.now())
admin.site.register(ExpiredEvent,ExpiredEventAdmin)  

