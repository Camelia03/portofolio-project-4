from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Thread(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True, blank=True)
    edited_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    @property
    def votes(self):
        return self.upvotes.count()-self.downvotes.count()


class Reply(models.Model):

    thread = models.ForeignKey(
        Thread, related_name='replies', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


# Upvote and Downvote model
class Upvote(models.Model):
    thread = models.ForeignKey(Thread, related_name='upvotes',
                               on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('thread', 'user')


class Downvote(models.Model):
    thread = models.ForeignKey(Thread, related_name='downvotes',
                               on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('thread', 'user')


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    avatar = CloudinaryField('image')

    def __str__(self):
        return self.user.username
