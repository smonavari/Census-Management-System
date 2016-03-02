from django.db import models


class ProtectedCountry(models.Model):
    name_country = models.CharField(null=False, blank=False, max_length=100)

    def __str__(self):
        return "{}".format(self.name_country)
