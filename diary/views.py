from django.views import generic
from django.urls import reverse_lazy


from .models import Entry


class EntryList(generic.ListView):
    template_name = "diary/entry_list.html"
    queryset = Entry.objects.all()
    context_object_name = "entries"


class EntryDetailView(generic.DetailView):
    model = Entry
    template_name = "diary/entry_detail.html"


class EntryCreateView(generic.CreateView):
    model = Entry
    template_name = "diary/entry_new.html"
    fields = "__all__"


class EntryUpdateView(generic.UpdateView):
    model = Entry
    fields = "__all__"
    template_name = "diary/entry_edit.html"


class EntryDeleteView(generic.DeleteView):
    model = Entry
    success_url = reverse_lazy("entry_list")
