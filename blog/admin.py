from django.contrib import admin
from blog.models import Ticket, Review, UserFollows


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'time_created')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'rating', 'user', 'time_created')


class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ('user', 'followed_user')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserFollows, UserFollowsAdmin)
