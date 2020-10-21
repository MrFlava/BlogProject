from django.contrib import admin

from newsfeed.models import Subscriber

# Register your models here.


class SubscriberAdmin(admin.ModelAdmin):
    model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)


