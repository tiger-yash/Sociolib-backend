from django.db import models
from django.conf import settings

def get_cover_image_filepath(self, filename):
    return 'profile_images/' + str(self.pk) + '/profile_image.png'


def get_default_cover_image():
    return "sample/Full-Moon.jpg"

# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=50, unique=True)
    genre = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    cover_image = models.ImageField(max_length=255, upload_to=get_cover_image_filepath,
                                      null=True, blank=True, default=get_default_cover_image)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Reviews(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="critic")
    book = models.ForeignKey(
        settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="reviewed_book")
    comment = models.CharField(max_length=280)
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    is_owned = models.BooleanField(default=False)

    def __str__(self):
        return self.book.name