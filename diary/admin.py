from django.contrib import admin
from .models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "slug", "public")
    list_filter = ("created_on", "author")
    raw_id_fields = ("author",)
    date_hierarchy = "created_on"
    ordering = ("-created_on",)

