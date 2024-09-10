from django.urls import reverse

from tests.helpers.pet_helpers import create_valid_pet
from tests.test_base import TestBase


class PetEditViewTest(TestBase):
    def test_get_edit__when_owner__expect_200_with_correct_pet_and_template(self):
        user = self._create_user()
        pet = create_valid_pet(user)

        self.client.login(**self.USER_DATA)
        response = self.client.get(
            reverse(
                "edit_pet",
                kwargs={
                    "username": self.USER_DATA["email"],
                    "pet_slug": pet.slug,
                }
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pets/pet-edit-page.html")