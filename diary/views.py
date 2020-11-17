from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Entry


class EntryList(generic.ListView):
    template_name = "diary/entry_list.html"
    queryset = Entry.objects.all()
    context_object_name = "entries"


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
