from unittest.mock import patch

from django.urls import reverse
from rest_framework import test

from recipes.tests.test_recipe_base import RecipeMixin


class RecipeAPIv2Test(test.APITestCase, RecipeMixin):

    def get_recipe_api_list(self):

        api_url = reverse('recipes:recipes-api-list')

        return self.client.get(api_url)

    def test_recipe_api_list_returns_status_code_200(self):

        response = self.get_recipe_api_list()
        self.assertEqual(
            response.status_code,
            200
        )

    @patch('recipes.views.api.RecipeAPIv2Pagination.page_size', new=7)
    def test_recipe_api_list_loads_correct_number_of_recipes(self):
        wanted_recipes = 7
        self.make_recipe_in_batch(qtd=wanted_recipes)
        response = self.client.get(
            reverse('recipes:recipes-api-list')+'?page=1')
        qtd_recipes_received = len(response.data.get('results'))
        self.assertEqual(
            wanted_recipes,
            qtd_recipes_received
        )

    def test_recipe_api_list_do_not_show_published_recipes(self):
        recipes = self.make_recipe_in_batch(qtd=2)
        recipe_not_published = recipes[0]
        recipe_not_published.is_published = False
        recipe_not_published.save()
        response = self.get_recipe_api_list()
        self.assertEqual(
            len(response.data.get('results')),
            1
        )
