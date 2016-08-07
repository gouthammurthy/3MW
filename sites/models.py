from django.db import models


# Creating models
class Site(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Detail(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=50, default='zzzz')
    date = models.CharField(max_length=50, default='99 Dec, 9999')
    a_value = models.DecimalField(max_digits=10, decimal_places=2)
    b_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.site.name + ' - ' + self.date
