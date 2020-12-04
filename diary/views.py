from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User


from .models import Entry


class EntryList(generic.ListView):
    template_name = "diary/entry_list.html"
    queryset = Entry.objects.all().filter(public=True)
    context_object_name = "entries"
    paginate_by = 5


class EntryPrivateListView(generic.ListView):
    template_name = "diary/entry_private_list.html"
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
    fields = ["title", "text", "public"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Entry
    fields = ["title", "text", "public"]
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


# class CalendarView(generic.ListView):
#     model = Entry
#     template_name = "partials/_calendar.html"
#     success_url = reverse_lazy("calendar")

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         d = get_date(self.request.GET.get("month", None))
#         cal = Calendar(d.year, d.month)
#         html_cal = cal.formatmonth(withyear=True)
#         context["calendar"] = mark_safe(html_cal)
#         context["prev_monht"] = prev_month(d)
#         context["next_month"] = next_month(d)

#         return context
