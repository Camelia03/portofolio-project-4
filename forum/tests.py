from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


from .models import Channel, Downvote, Thread, Upvote

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


class ThreadEditViewTest(TestCase):
    """Test that the edit thread view work correctly"""

    @classmethod
    def setUpTestData(self):
        self.user = create_test_user()
        self.channel = create_test_channel()

    def setUp(self):
        self.client.login(username=self.user.username, password=user_password)
        self.thread = Thread.objects.create(
            title='Test Thread',
            content="Test content",
            user=self.user,
            channel=self.channel
        )
        self.thread.save()

    def test_renders_correct_template(self):
        """Test that the edit thread form is rendered correctly"""

        response = self.client.get(reverse('thread_edit', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thread_edit.html')

    def test_thread_can_be_edited(self):
        """Test that the thread can be edited"""

        new_title = 'Different title'

        response = self.client.post(
            reverse('thread_edit', kwargs={'pk': 1}),
            {
                'title': new_title,
                'content': self.thread.content,
                'channel': self.channel.id
            }
        )

        thread = Thread.objects.get(title=new_title)

        self.assertEqual(thread.title, new_title)
        self.assertRedirects(
            response, reverse('thread_detail', kwargs={'pk': self.thread.id})
        )

    def test_404_is_returned_for_wrong_thread(self):
        """Test that 404 is shown when trying to edit a wrong thread"""

        response = self.client.get(reverse('thread_edit', kwargs={'pk': 100}))

        self.assertEqual(response.status_code, 404)

    def test_user_can_only_edit_own_threads(self):
        """Test that a user can only edit his threads"""

        other_user = User.objects.create_user(
            username='otheruser', password='password'
        )
        other_user.save()

        other_thread = Thread.objects.create(
            title='Test Thread',
            content="Test content",
            user=other_user,
            channel=self.channel
        )
        other_thread.save()

        response = self.client.get(reverse('thread_edit', kwargs={'pk': 2}))

        self.assertEqual(response.status_code, 403)


class UserProfileViewTest(TestCase):
    """Test the user profile view"""

    @classmethod
    def setUpTestData(self):
        self.user = create_test_user()

    def setUp(self):
        self.client.login(username=self.user.username, password=user_password)

    def test_renders_correct_template(self):
        """Test that the profile template is rendered correctly"""

        response = self.client.get(reverse('user_profile'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertContains(response, self.user.username)


class UserPublicProfileViewTest(TestCase):
    """Test the user public profile view"""

    @classmethod
    def setUpTestData(self):
        self.user = create_test_user()

    def setUp(self):
        self.client.login(username=self.user.username, password=user_password)

    def test_renders_correct_template(self):
        """Test that the profile template is rendered correctly"""

        response = self.client.get(
            reverse('public_profile', kwargs={'username': self.user.username})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'public_profile.html')
        self.assertContains(response, self.user.username)


class UserThreadsViewTest(TestCase):
    """Test the user threads view"""

    @classmethod
    def setUpTestData(self):
        self.user = create_test_user()

    def setUp(self):
        self.client.login(username=self.user.username, password=user_password)

    def test_renders_correct_template(self):
        """Test that the profile template is rendered correctly"""

        response = self.client.get(
            reverse('user_threads')
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_threads.html')

    def test_only_users_threads_are_shown(self):
        """Test that only the logged in users thread are shown"""

        other_user = User.objects.create_user(
            username='other_user', password='password'
        )
        other_user.save()

        channel = create_test_channel()

        # Create 5 threads for the logged in user
        for i in range(5):
            thread = Thread.objects.create(
                title='Test Thread ${i} Batch1',
                content="Test content",
                user=self.user,
                channel=channel
            )
            thread.save()

        # Create 3 threads for the other user
        for i in range(3):
            thread = Thread.objects.create(
                title='Test Thread ${i} Batch1',
                content="Test content",
                user=other_user,
                channel=channel
            )
            thread.save()

        response = self.client.get(
            reverse('user_threads')
        )

        self.assertQuerysetEqual(
            response.context['thread_list'],
            Thread.objects.filter(user=self.user).order_by('-created_on')
        )


class UpvoteThreadViewTest(TestCase):
    """Test the upvote view"""

    @classmethod
    def setUpTestData(self):
        self.user = create_test_user()
        self.channel = create_test_channel()

        other_user = User.objects.create_user(
            username='other_user', password='password'
        )
        other_user.save()

        self.thread = Thread.objects.create(
            title='Test Thread',
            content="Test content",
            user=other_user,
            channel=self.channel
        )
        self.thread.save()

    def setUp(self):
        self.client.login(username=self.user.username, password=user_password)

    def test_upvote_thread(self):
        """Test that a user can upvote a thread"""

        response = self.client.post(reverse('upvote_thread', kwargs={'pk': 1}))
        upvote = Upvote.objects.get(user=self.user, thread=self.thread)

        self.assertIsNotNone(upvote)
        self.assertRedirects(
            response, reverse('thread_detail', kwargs={'pk': 1})
        )


class DownvoteThreadViewTest(TestCase):
    """Test the downvote view"""

    @classmethod
    def setUpTestData(self):
        self.user = create_test_user()
        self.channel = create_test_channel()

        other_user = User.objects.create_user(
            username='other_user', password='password'
        )
        other_user.save()

        self.thread = Thread.objects.create(
            title='Test Thread',
            content="Test content",
            user=other_user,
            channel=self.channel
        )
        self.thread.save()

    def setUp(self):
        self.client.login(username=self.user.username, password=user_password)

    def test_upvote_thread(self):
        """Test that a user can downvote a thread"""

        response = self.client.post(
            reverse('downvote_thread', kwargs={'pk': 1})
        )
        downvote = Downvote.objects.get(user=self.user, thread=self.thread)

        self.assertIsNotNone(downvote)
        self.assertRedirects(
            response, reverse('thread_detail', kwargs={'pk': 1})
        )


class ThreadDeleteViewTest(TestCase):
    """Test the delete thread functionality"""

    @classmethod
    def setUpTestData(self):
        self.user = create_test_user()
        self.channel = create_test_channel()

    def setUp(self):
        self.client.login(username=self.user.username, password=user_password)

        for i in range(2):
            thread = Thread.objects.create(
                title=f'Test Thread ${i}',
                content="Test content",
                user=self.user,
                channel=self.channel
            )
            thread.save()

    def test_thread_can_be_deleted(self):
        """Test that a thread can be deleted"""

        response = self.client.post(reverse('thread_delete'), {'thread_id': 1})

        threads = Thread.objects.all()

        # Ensure only the second thread is left
        self.assertEqual(threads[0].id, 2)
        self.assertRedirects(response, reverse('user_threads'))

    def test_returns_404_for_wrong_thread(self):
        """Tests that 404 is returned for the wrong thread id"""

        response = self.client.post(
            reverse('thread_delete'), {'thread_id': 100}
        )
        self.assertEqual(response.status_code, 404)

    def test_user_can_only_delete_own_thread(self):
        """Test that the a use can only delete his own threads"""

        other_user = User.objects.create_user(
            username='otheruser', password='password'
        )
        other_user.save()

        other_thread = Thread.objects.create(
            title='Test Thread',
            content="Test content",
            user=other_user,
            channel=self.channel
        )
        other_thread.save()

        response = self.client.post(
            reverse('thread_delete'), {'thread_id': other_thread.id}
        )

        self.assertEqual(response.status_code, 403)


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
