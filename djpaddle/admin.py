from django.contrib import admin

from .models import Checkout, Plan, Price

admin.site.register(Checkout)


class PriceInline(admin.TabularInline):
    model = Price


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    inlines = (PriceInline,)
    list_display = (
        "id",
        "name",
    )


#@admin.register(models.Subscription)
#class SubscriptionAdmin(admin.ModelAdmin):
#    list_display = (
#        "subscriber",
#        "email",
#        "status",
#        "plan",
#    )
#    list_filter = (
#        "status",
#        "plan",
#    )
#    search_fields = [
#        'email',
#    ]
#    autocomplete_fields = (
#        "subscriber",
#    )
