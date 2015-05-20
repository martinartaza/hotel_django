from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    logo = models.ImageField(
        upload_to='carpeta_imagen/hotel/',
        default='carpeta_imagen/no-img.jpg')
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.name + ' ' + self.title

    def was_hotel_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_hotel_published_recently.admin_order_field = 'pub_date'
    was_hotel_published_recently.boolean = True
    was_hotel_published_recently.short_description = 'Published recently?'


class Galery(models.Model):
    hotel = models.ForeignKey(Hotel)
    description_text = models.CharField(max_length=200)
    image_galery = models.ImageField(
        upload_to='hotel_galery/',
        default='hotel_galery/no-img.jpg')


class Ranking(models.Model):
    hotel = models.ForeignKey(Hotel)
    description_text = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice_text
