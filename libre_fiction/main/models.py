from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_nh3.models import Nh3TextField


User = get_user_model()


class Book(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name=_('Book'),
        related_name='books',
        on_delete=models.CASCADE,
    )
    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'), blank=True)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    views_count = models.PositiveIntegerField(_('Views count'), default=0)
    likes_count = models.PositiveIntegerField(_('Likes count'), default=0)
    is_published = models.BooleanField(_('Is published'), default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return self.title


class Chapter(models.Model):
    book = models.ForeignKey(
        Book,
        verbose_name=_('Book'),
        related_name='chapters',
        on_delete=models.CASCADE,
    )
    title = models.CharField(_('Title'), max_length=255)
    content = Nh3TextField(
        _('Content'),
        allowed_tags=settings.ALLOWED_HTML_TAGS,
        allowed_attributes=settings.ALLOWED_HTML_ATTRIBUTES,
        url_schemes=settings.ALLOWED_URL_SCHEMES,
        strip_comments=True,
    )
    order = models.PositiveIntegerField(_('Order'), default=0)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = _('Chapter')
        verbose_name_plural = _('Chapters')

    def save(self, *args, **kwargs):
        if not self.pk:
            max_order = Chapter.objects.filter(
                book=self.book
            ).aggregate(models.Max('order'))['order__max']
            self.order = (max_order or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_('User'),
        related_name='likes',
        on_delete=models.CASCADE,
    )
    book = models.ForeignKey(
        Book,
        verbose_name='Book',
        related_name='likes',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
