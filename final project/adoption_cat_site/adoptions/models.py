from django.db import models
import datetime
from django.utils import timezone
import random
import string
from users.forms import User

def rename_upload_photo(instance, filename):
    filename_splited = filename.split(".")
    photo_extension = filename_splited[1]
    new_filename = ""
    for letter in filename_splited[0]:
        new_filename += random.choice(string.ascii_letters)
    return "adoptions/" + new_filename + "." + photo_extension

class Cat(models.Model):
    cat_name_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    adoption_date = models.DateTimeField('date adopted', default=timezone.now())
    adopted = models.BooleanField(default=False)
    human = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.cat_name_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    

class Cat_Details(models.Model):

    details = models.ForeignKey(Cat, on_delete=models.CASCADE)
    description_text = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    location = models.CharField(max_length=200)
    cat_photo = models.ImageField(upload_to=rename_upload_photo, default='static/adoptions/cat_static.jpg')

    def __str__(self):
        return self.description_text


