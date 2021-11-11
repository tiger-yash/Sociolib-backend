from django.db import models
from django.conf import settings

def get_cover_image_filepath(self, filename):
    return 'book_images/' + str(self.pk) + '/book_image.png'


def get_default_cover_image():
    return "sample/book.jpg"

# Create your models here.
class Reviews(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="critic")
    comment = models.CharField(max_length=280)
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    is_owned = models.BooleanField(default=False)

    def __str__(self):
        return self.comment
class BookInfo(models.Model):
    name = models.CharField(max_length=50, unique=True)
    genre = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    cover_image = models.ImageField(max_length=255, upload_to=get_cover_image_filepath,
                                      null=True, blank=True, default=get_default_cover_image)
    price = models.IntegerField(default=0)
    book_review=models.ManyToManyField(Reviews,blank=True, related_name='customer_reviews',)
    summary= models.CharField(max_length=1000,null=True)
    def __str__(self):
        return self.name

