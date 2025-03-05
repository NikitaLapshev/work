from django.test import TestCase, Client

from django.contrib.auth import get_user_model
from django.utils import timezone

from task.models import Task

User = get_user_model()


class TaskListViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username="Test", email="test@test.test")
        self.task = Task.objects.create(owner=self.user, title="test", deadline=timezone.now())

    def test_login_required(self):
        """Test login required for View """
        response = self.client.get("/")

        self.assertEqual(response.status_code, 302)

    def test_get_queryset(self):
        """Test get queryset for View"""

        self.client.login(username=self.user.username, password=self.user.password)

        response = self.client.get("/")

        print(response)