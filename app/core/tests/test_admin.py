from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    # setup fucntion, sometimes set up tasks need to be run before every
    # test in testcase class
    def setUp(self):
        """ create test users for subsequent tests"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@nyu.edu',
            password='pass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@nyu.edu',
            password='test123',
            name='test user'
        )

    def test_users_listed(self):
        """test users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        # res = response
        res = self.client.get(url)  # http get

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """test user edit page works"""
        # reverse function will create this url -> /admin/core/user/user_id
        url = reverse('admin:core_user_change', args=[self.user.id])

        res = self.client.get(url)

        # test that the page renders okay by below
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """test that create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
