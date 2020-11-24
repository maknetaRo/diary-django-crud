from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth.models import User


from .models import Entry


class EntryList(generic.ListView):
    template_name = "diary/entry_list.html"
    queryset = Entry.objects.all()
    context_object_name = "entries"


class EntryPrivateListView(generic.ListView):
    template = "diary/entry_private_list.html"
    context_object_name = "entries"
    paginate_by = 5

    def get_queryset(self):
        queryset = Entry.objects.all()
        user = self.request.user

        if not user.is_anonymous:
            queryset = queryset.filter(author=user)
        return queryset


class EntryDetailView(generic.DetailView):
    model = Entry
    template_name = "diary/entry_detail.html"


class EntryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Entry
    template_name = "diary/entry_new.html"
    fields = "__all__"


class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Entry
    fields = "__all__"
    template_name = "diary/entry_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Entry
    success_url = reverse_lazy("entry_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

