from django.db import models
from django.conf import settings



User = settings.AUTH_USER_MODEL

class Post(models.Model):

    title = models.CharField(max_length=30)
    description = models.TextField()
    author = models.ForeignKey('Author', on_delete= models.CASCADE)
    image = models.ImageField(upload_to="profile_pic")
    timestamp = models.DateField(auto_now=True)
    add_time = models.DateField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title




# Create your models here.
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    cellphone_num = models.IntegerField()

    def __str__(self):
        return self.user.username


