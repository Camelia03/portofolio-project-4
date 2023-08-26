from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Channel(models.Model):
    """Channel model"""

    name = models.CharField(max_length=100)
    image = CloudinaryField('image')
    icon = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Thread(models.Model):
    """Thread model"""

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='threads')
    image = CloudinaryField('image', null=True, blank=True)
    edited_on = models.DateTimeField(auto_now=True)
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name='threads')

    def __str__(self) -> str:
        return self.title

    @property
    def votes(self):
        """Calculate the number of votes"""
        return self.upvotes.count()-self.downvotes.count()


class Reply(models.Model):
    """Reply model"""

    thread = models.ForeignKey(
        Thread, related_name='replies', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


class Upvote(models.Model):
    """Upvote model"""

    thread = models.ForeignKey(Thread, related_name='upvotes',
                               on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Ensure only one upvote per user and thread"""

        unique_together = ('thread', 'user')


class Downvote(models.Model):
    """Downvote model"""

    thread = models.ForeignKey(Thread, related_name='downvotes',
                               on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Ensure only one downvote per user and thread"""

        unique_together = ('thread', 'user')


class Profile(models.Model):
    """Profile model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    avatar = CloudinaryField('image')

    def __str__(self):
        return self.user.username
