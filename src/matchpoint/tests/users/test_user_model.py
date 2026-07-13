from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase

from users.models import CustomUser


class CustomUserModelTestCase(TestCase):
    def setUp(self) -> None:
        self.user = CustomUser.objects.create_user(
            email="test@test.com", password="12test34"
        )
        self.superuser = CustomUser.objects.create_superuser(
            email="superuser@test.com", password="12test34"
        )

    def test_user_creation_creates_user(self):
        self.assertEqual(1, CustomUser.objects.filter(is_staff=False).count())
        self.assertEqual(self.user.email, "test@test.com")
        self.assertIsNotNone(self.user.password)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_superuser_creation_creates_superuser(self):
        self.assertEqual(1, CustomUser.objects.filter(is_staff=True).count())
        self.assertEqual(self.superuser.email, "superuser@test.com")
        self.assertIsNotNone(self.superuser.password)
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_superuser)

    def test_create_user_with_same_name_raises(self):
        with self.assertRaises(IntegrityError) as e:
            CustomUser.objects.create_user(email="test@test.com", password="12test34")
