from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django_peeringdb.models.concrete import NetworkIXLan


@python_2_unicode_compatible
class Peering(models.Model):
    netixlan = models.OneToOneField(NetworkIXLan, db_index=True)
    router = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return "Peering with {} on {}".format(
                self.netixlan.net.name,
                self.netixlan.ixlan.ix.name
            )
