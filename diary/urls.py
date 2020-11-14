from django.urls import path

from . import views

urlpatterns = [
    path("", views.EntryList.as_view(), name="entry_list"),
    path("entry/new/", views.EntryCreateView.as_view(), name="entry_new"),
    path(
        "entry/<slug:slug>/delete/",
        views.EntryDeleteView.as_view(),
        name="entry_delete",
    ),
    path("entry/<slug:slug>/edit/", views.EntryUpdateView.as_view(), name="entry_edit"),
    path("entry/<slug:slug>/", views.EntryDetailView.as_view(), name="entry_detail",),
]
