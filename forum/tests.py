from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Channel, Thread

user_password = 'password'


def create_test_user():
    username = 'test_user'
    password = user_password

    user = User.objects.create_user(
        username=username, password=password
    )
    user.save()

    return user


def create_test_channel():
    channel = Channel.objects.create(
        name="Test channel",
        slug="test-channel"
    )
    channel.save()
    return channel


class IndexAllViewTest(TestCase):
    """Test list threads cases when no channel is selected"""

    @classmethod
    def setUpTestData(self):
        self.user = create_test_user()

        channel = create_test_channel()
        self.channel = channel

    def setUp(self):
        self.client.login(
            username=self.user.username,
            password=user_password
        )

        for i in range(10):
            thread = Thread.objects.create(
                title="Test Thread",
                content="Test Model",
                user=self.user,
                channel=self.channel
            )
            thread.save()

    def test_renders_correct_template(self):
        """Test if the index path renders with the correct template"""

        response = self.client.get(reverse('index'))

        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, "All Threads", status_code=200)

    def test_correct_threads_shown(self):
        """
        Test that max 5 threads are returned
        and are ordered descending by the creation date
        """

        response = self.client.get(reverse('index'))

        self.assertQuerysetEqual(
            response.context['thread_list'],
            Thread.objects.all().order_by('-created_on')[:5]
        )

    def test_correct_nr_of_total_thread(self):
        """Test that the total nr of threads is correct"""

        response = self.client.get(reverse('index'))

        self.assertEqual(response.context['total_threads_nr'], 10)

    def test_channels_are_shown(self):
        """Test that channels are shown"""

        response = self.client.get(reverse('index'))

        self.assertQuerysetEqual(
            response.context['channels'], Channel.objects.all()
        )
        self.assertContains(response, self.channel.name)
