from django.db import models


class Language(models.Model):
    name_text = models.CharField(max_length=200)
    css_class_text = models.CharField(max_length=200)

    def __str__(self):
        return self.name_text


class Project(models.Model):
    name_text = models.CharField(max_length=200)
    url_text = models.CharField(max_length=200)
    description_text = models.TextField()
    pub_date = models.DateTimeField("date published")
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name_text
