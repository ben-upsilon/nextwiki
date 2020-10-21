from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify


class Article(models.Model):
    title = models.CharField(max_length=1024, default="new title", null=False)
    slug = models.SlugField(max_length=50, unique=True)
    content = models.TextField(help_text="Formatted using Markdown")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False, verbose_name="Publish?")
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return 'wiki_article_detail', (), {'slug': self.slug}


class Edit(models.Model):
    """Stores an edit session"""

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    edited_on = models.DateTimeField(auto_now_add=True)
    summary = models.CharField(max_length=100)

    class Meta:
        ordering = ['-edited_on']

    def __str__(self):
        return "%s - %s - %s" % (self.summary, self.editor, self.edited_on)

    def get_absolute_url(self):
        return 'wiki_edit_detail', self.id
