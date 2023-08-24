from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


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


class ChannelThreadsViewTest(TestCase):
    """Test list threads cases when a channel is selected"""

    @classmethod
    def setUpTestData(self):
        self.user = create_test_user()

    def setUp(self):
        self.client.login(
            username=self.user.username,
            password=user_password
        )

        channel = Channel.objects.create(
            name="Test channel",
            slug="test-channel"
        )
        channel.save()

        for i in range(10):
            thread = Thread.objects.create(
                title="Test Thread",
                content="Test Model",
                user=self.user,
                channel=channel
            )
            thread.save()

        channel = Channel.objects.create(
            name="Test channel 2",
            slug="test-channel-2"
        )
        channel.save()

        for i in range(5):
            thread = Thread.objects.create(
                title="Test Thread",
                content="Test Model",
                user=self.user,
                channel=channel
            )
            thread.save()

    def test_renders_correct_template(self):
        """Test that the channel name appears in the correct template"""

        channel = Channel.objects.get(id=1)

        response = self.client.get(
            reverse('channel_threads', kwargs={
                    'name': channel.slug})
        )

        self.assertContains(response, channel.name, status_code=200)
        self.assertTemplateUsed(response, "index.html")

    def test_only_channel_threads_shown(self):
        """Test that only the threads in the selected channel are shown"""

        channel = Channel.objects.get(id=2)

        response = self.client.get(
            reverse('channel_threads', kwargs={
                    'name': channel.slug})
        )

        self.assertQuerysetEqual(
            response.context['thread_list'],
            Thread.objects.filter(channel=channel).order_by('-created_on')
        )


class ThreadDetailViewTest(TestCase):
    """Test the thread details view"""

    @classmethod
    def setUpTestData(self):
        self.user = create_test_user()
        self.channel = create_test_channel()
        self.thread = Thread.objects.create(
            title="Test Thread",
            content="Test Model",
            user=self.user,
            channel=self.channel
        )
        self.thread.save()

    def setUp(self):
        self.client.login(username=self.user.username, password=user_password)
        pass

    def test_thread_shown_with_correct_template(self):
        """Test that the thread is shown using the correct template"""

        response = self.client.get(
            reverse('thread_detail', kwargs={'pk': self.thread.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.thread.title)
        self.assertContains(response, self.thread.content)
        self.assertTemplateUsed(response, "thread_detail.html")

    def test_returns_404_for_wrong_threads(self):
        """Tests that 404 is returned for wrong thread ids"""

        response = self.client.get(
            reverse('thread_detail', kwargs={'pk': 500})
        )

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")


class ThreadAddViewTest(TestCase):
    """Test the add thread view"""

    @classmethod
    def setUpTestData(self):
        self.user = create_test_user()
        self.channel = create_test_channel()

    def setUp(self):
        self.client.login(username=self.user.username, password=user_password)

    def test_form_shown_with_correct_template(self):
        """
        Test that the add thread form is shown using the correct template
        and no channel
        """

        response = self.client.get(reverse('thread_add'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "thread_add.html")
        self.assertIsNone(
            response.context['form'].fields['channel'].initial
        )

    def test_form_has_channel_pre_filled(self):
        """
        Test that the add thread form has the channel prefilled
        with the query param value
        """

        response = self.client.get(
            reverse('thread_add') + '?channel=test-channel'
        )

        self.assertEqual(
            response.context['form'].fields['channel'].initial,
            self.channel
        )

    def test_returns_404_for_wrong_channel(self):
        """
        Test that the add thread form has the channel prefilled
        with the query param value
        """

        response = self.client.get(
            reverse('thread_add') + '?channel=fake-channel'
        )

        self.assertEqual(response.status_code, 404)

    def test_invalid_thread_is_not_created(self):
        """Test thread validation works"""

        response = self.client.post(
            reverse('thread_add'),
            {
                'title': 'My thread',
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'content',
                             ['This field is required.'])

        with self.assertRaises(Thread.DoesNotExist):
            Thread.objects.get(title='My thread')

    def test_valid_thread_is_created(self):
        """Test thread can be created"""

        response = self.client.post(
            reverse('thread_add'),
            {
                'title': 'My thread',
                'content': 'Test Content',
                'channel': self.channel.id,
            }
        )

        self.assertRedirects(response, reverse('index'))
        self.assertEqual(
            Thread.objects.get(title='My thread').title,
            'My thread'
        )

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Your thread was created successfully.'
        )


class ThreadSearchViewTest(TestCase):
    """Test that the search view work correctly"""

    @classmethod
    def setUpTestData(self):
        self.user = create_test_user()
        channel = create_test_channel()

        for i in range(10):
            thread = Thread.objects.create(
                title='Test Thread ${i} Batch1',
                content="Test content",
                user=self.user,
                channel=channel
            )
            thread.save()

        channel = Channel.objects.create(
            name="Test channel 2",
            slug="test-channel-2"
        )
        channel.save()

        for i in range(5):
            thread = Thread.objects.create(
                title=f'Test Thread ${i} Batch2',
                content="Test content",
                user=self.user,
                channel=channel
            )
            thread.save()

    def setUp(self):
        self.client.login(username=self.user.username, password=user_password)

    def test_renders_correct_template(self):
        response = self.client.get(reverse('thread_search'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')

    def test_bad_search_returns_nothing(self):
        response = self.client.get(reverse('thread_search') + '?keyword=wrong')

        self.assertQuerysetEqual(response.context['threads'], [])
        self.assertContains(response, '0 Results')

    def test_bad_search_returns_correct_threads(self):
        response = self.client.get(
            reverse('thread_search') + '?keyword=batch2')

        self.assertQuerysetEqual(
            response.context['threads'],
            Thread.objects.filter(title__icontains='batch2')
        )
        self.assertContains(response, '5 Results')


class UnauthorizedViewsTest(TestCase):
    """Test that all views that require authentication redirect to login"""

    def setUp(self):
        pass

    def test_index_requires_login(self):
        """Test that the index path redirects to login"""

        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('login')))

    def test_channel_threads_requires_login(self):
        """Test that the index path redirects to login"""

        response = self.client.get(
            reverse('channel_threads', kwargs={'name': 'test'})
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('login')))

    def test_thread_detail_requires_login(self):
        """Test that the thread detail path redirects to login"""

        response = self.client.get(
            reverse('thread_detail', kwargs={'pk': '1'})
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('login')))
