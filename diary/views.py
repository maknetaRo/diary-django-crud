from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


from .models import Entry


class EntryList(generic.ListView):
    template_name = "diary/entry_list.html"
    queryset = Entry.objects.all()
    context_object_name = "entries"
    paginate_by = 5

    def get_queryset(self, **kwargs):
        qs = Entry.objects.filter(public=True)
        # qs_public = Entry.objects.filter(public=True)
        # user = self.user
        # entry = self.entry
        # if user.is_authenticated and user == entry.author:
        #     qs_author = Entry.objects.filter("author")
        # qs = qs_public | qs_author

        return qs


# class EntryListByAuthor(generic.ListView):


class EntryDetailView(generic.DetailView):
    model = Entry
    template_name = "diary/entry_detail.html"


class EntryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Entry
    template_name = "diary/entry_new.html"
    fields = "__all__"


class EntryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Entry
    fields = "__all__"
    template_name = "diary/entry_edit.html"


class EntryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Entry
    success_url = reverse_lazy("entry_list")

