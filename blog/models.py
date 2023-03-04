from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    
    slug = models.SlugField(_('Slug'))
    
    text = models.TextField(_('Text'))
    
    author = models.ForeignKey(get_user_model(), verbose_name=_('Author'), on_delete=models.CASCADE)
    
    status = models.BooleanField(default=False)
    
    
    datetime_created = models.DateTimeField(_('datetime_created'), default=timezone.now())
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime_modified'))
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])