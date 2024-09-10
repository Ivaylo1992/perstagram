from django.urls import reverse
from django.utils.text import slugify

from petstagram3.pets.models import Pet
from tests.helpers.pet_helpers import PET_DATA
from tests.test_base import TestBase


class PetCreateViewTest(TestBase):
    def test_get_create__when_logged_in_user__expect_200_and_correct_template(self):
        self._create_user()
        self.client.login(**self.USER_DATA)

        response = self.client.get(reverse("add_pet"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pets/pet-add-page.html")

    def test_get_create__when_anonymous_user_expect_302_with_redirect_to_login(self):
        create_pet_url = reverse("add_pet")
        login_url = reverse("login")

        response = self.client.get(create_pet_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f"{login_url}?next={create_pet_url}"
        )


    def test_post_create__when_logged_in_user__expect_302_with_correct_redirect_and_create_pet_with_correct_slug(self):
        self._create_user()
        self.client.login(**self.USER_DATA)

        response = self.client.post(
            reverse("add_pet"),
            data=PET_DATA
        )

        created_pet = Pet.objects.get(**PET_DATA)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse(
                "pet_details",
                kwargs={
                    "username": self.USER_DATA["email"],
                    "pet_slug": created_pet.slug
                }
            )
        )

        self.assertEqual(
            slugify(
                f"{created_pet.name}-{created_pet.pk}"
            ),
            created_pet.slug,
        )

    def test_post_create__when_anonymous_user__expect_302_with_redirect_to_login(self):
        create_pet_url = reverse("add_pet")
        login_url = reverse("login")

        response = self.client.post(
            create_pet_url,
            data=PET_DATA,
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            f"{login_url}?next={create_pet_url}"
        )