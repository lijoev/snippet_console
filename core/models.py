from django.contrib.auth.models import User
from django.db import models


class AbstractDateBase(models.Model):
    """
    Abstract Date base class for sub apps under core
    """
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractUserBase(models.Model):
    """
    Abstract User base class for sub apps under core
    """
    created_by = models.ForeignKey(User,
                                   related_name='%(class)s_createdby',
                                   blank=True, null=True,
                                   on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User,
                                    related_name='%(class)s_modifiedby',
                                    null=True, blank=True,
                                    on_delete=models.SET_NULL)

    class Meta:
        abstract = True
