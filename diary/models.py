from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


def generate_unique_slug(klass, field):
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{origin_slug}-{numb}"
        numb += 1
    return unique_slug


class Entry(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, default="", editable=False)
    image = models.ImageField(upload_to="diary", blank=True, null=True)
    text = RichTextUploadingField(max_length=50000, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_on",)
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {"slug": self.slug}
        return reverse("entry_detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.slug:
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Entry, self.title)
            else:
                self.slug = generate_unique_slug(Entry, self.title)
        super(Entry, self).save(*args, **kwargs)

