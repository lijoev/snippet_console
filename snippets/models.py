from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import AbstractDateBase, AbstractUserBase


class Tag(models.Model):
    """
    Tag model
    """
    title = models.CharField(verbose_name=_('title'), max_length=100,
                             unique=True, null=False, blank=False)

    def __str__(self):
        return self.title


class ShortSnippet(AbstractDateBase, AbstractUserBase):
    """
    Model class for saving short snippets
    """
    title = models.CharField(verbose_name=_('title'), max_length=300,
                             null=False, blank=False)
    description = models.TextField(verbose_name=_('description'), null=True,
                                   blank=True)
    tag = models.ForeignKey(Tag, null=True, blank=True,
                            on_delete=models.SET_NULL, verbose_name=_('tag'))

    def __str__(self):
        return self.title





