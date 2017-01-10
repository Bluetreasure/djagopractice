from django.contrib import admin
from hanktest.models import Profile
from hanktest.models import Poll
from hanktest.models import PollItem

# Register your models here.


class PollAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'enabled')
    ordering = ('-created_at',)


class PollItemAdmin(admin.ModelAdmin):
    list_display = ('poll', 'name', 'vote', 'image_url')
    ordering = ('poll',)


admin.site.register(Profile)
admin.site.register(Poll, PollAdmin)
admin.site.register(PollItem, PollItemAdmin)
