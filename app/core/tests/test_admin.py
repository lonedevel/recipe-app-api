from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Test Admin Functions"""

    def setUp(self):
        email1 = 'admin@emaildomain.com'
        email2 = 'test@emaildomain.com'
        password = 'Testpass123'
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email=email1,
            password=password
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email=email2,
            password=password
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
