from io import BytesIO
from PIL import Image # Under Pillow library

from django.core.files import File
from django.db import models

from apps.vendor.models import Vendor


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'


    def make_thumbnail(self, image, size=(300, 200)):
        with Image.open(image) as img:
            # return a converted copy of the image, with the mode of RGB, a true color mode
            img.convert('RGB')
            img.thumbnail(size)
            # BytesIO() - a binary stream (file object) using an in-memory bytes buffer
            thumb_io = BytesIO()
            # The first save() param is called fp - which takes in filename (string), pathlib.Path object or file object.
            # JPEG's save() method supports quality param/option - default is 75
            img.save(thumb_io, 'JPEG', quality=85)
            # print(thumb_io.getvalue())

        # At this point, thumb_io has the bytes value of the image (try print as shown above)
        # It is then attached to a File class wrapper of Python's file object with name param
        # name = The name of the file including the relative path from MEDIA_ROOT
        # image.name = FieldFile.name (The name of the file including the relative path from the root of the Storage of the associated FileField)
        thumbnail = File(thumb_io, name=image.name)

        return thumbnail