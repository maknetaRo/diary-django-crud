from django import template
from ..models import Entry
from django.shortcuts import get_object_or_404

register = template.Library()


@register.simple_tag
def all_public_entries():
    return Entry.objects.filter(public=True).count()


@register.inclusion_tag("diary/all_entries.html")
def list_all_entries():
    all_enteries = Entry.objects.filter(public=True).order_by("-created_on")
    return {"all_entries": all_enteries}

