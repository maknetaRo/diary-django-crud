from django.contrib import admin
from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "slug", "public")
    readonly_fields = (
        "author",
        "image",
        "title",
        "text",
        "public",
    )
    list_filter = ("created_on", "author")
    raw_id_fields = ("author",)
    date_hierarchy = "created_on"
    ordering = ("-created_on",)

    def get_queryset(self, request):
        if request.user.is_superuser:
            queryset = Entry.objects.all().filter(public=True)
        else:
            try:
                queryset = Entry.objects.all().filter(author=request.user.id)
            except:
                queryset = Entry.objects.none()
        return queryset


admin.site.register(Entry, EntryAdmin)

