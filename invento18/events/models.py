from django.db import models
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    category_types = (
    ('gen', 'General'),
    ('cse', 'CSE'),
    ('ece', 'ECE'),
    ('eee', 'EEE'),
    ('it', 'IT'),
    ('me', 'ME'),
    ('sta','SAPTHA')
    )
    type_types=(
    ('wor', 'Workshops'),
    ('com', 'Competitions'),
    ('sho', 'Shows'),
    ('tal', 'Talks'),
    ('oth', 'Other'),
    )
    title = models.CharField(max_length=50)
    short_desc = models.TextField(max_length=500, default="something short")
    long_desc = models.TextField(max_length=2000,default="something long")
    category = models.CharField(max_length=3, default='gen', choices=category_types)
    _type = models.CharField(max_length=3, default='wor', choices=type_types, verbose_name="Type")
    fee = models.FloatField()# Set zero for free events
    prize = models.FloatField()
    coordinators = models.TextField(max_length=500)
    day = models.PositiveIntegerField()
    imageurl = models.URLField(blank=True)
    posterurl = models.URLField(blank=True)
    townscript_code = models.CharField(max_length=50, blank=True)
    pdfurl = models.URLField(blank=True)

    def admin_image(self):
        return self.imageurl
    admin_image.allow_tags = True
    
    def admin_poster(self):
        return self.posterurl
    admin_poster.allow_tags = True

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-view', kwargs={'pk':self.pk})

    def get_admin_url(self):
        return reverse("admin:%s_%s_change" % (self._meta.app_label, self._meta.model_name), args=(self.id,))


class Event_register(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email =  models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    referal_code = models.CharField(max_length=50)
    event = models.CharField(max_length=50)


class Ambassador(models.Model):
    referal_code = models.CharField(primary_key=True,max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email =  models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    college = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    points = models.IntegerField(default=0)
