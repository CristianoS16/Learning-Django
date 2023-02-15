from unittest.mock import patch

from django.urls import reverse
from rest_framework import test

from recipes.tests.test_recipe_base import RecipeMixin


class RecipeAPIv2Test(test.APITestCase, RecipeMixin):

    def get_recipe_reverse_url(self, reverse_result=None):
        return reverse(
            'recipes:recipes-api-list'
        ) if reverse_result is None else reverse_result

    def get_recipe_api_list(self, reverse_result=None):

        api_url = self.get_recipe_reverse_url(reverse_result)

        return self.client.get(api_url)

    def get_jwt_access_token(self):
        userdata = {
            'username': 'user',
            'password': 'fakepassword'
        }
        self.make_author(
            username=userdata.get("username"),
            password=userdata.get("password"),
        )
        response = self.client.post(
            reverse('recipes:token_obtain_pair'), data={**userdata})
        return response.data.get('access')

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

    @patch('recipes.views.api.RecipeAPIv2Pagination.page_size', new=10)
    def test_recipe_api_list_loads_recipes_by_category_id(self):
        category_wanted = self.make_category(name='WANTED_CATEGORY')
        category_not_wanted = self.make_category(name='NOT_WANTED_CATEGORY')
        recipes = self.make_recipe_in_batch(qtd=10)

        for recipe in recipes:
            recipe.category = category_wanted
            recipe.save()

        recipes[0].category = category_not_wanted
        recipes[0].save()

        api_url = reverse('recipes:recipes-api-list') + \
            f'?category_id={category_wanted.id}'
        response = self.get_recipe_api_list(reverse_result=api_url)
        self.assertEqual(
            len(response.data.get('results')),
            9
        )

    def test_recipe_api_list_user_must_send_JWT_token_to_create(self):
        api_url = self.get_recipe_reverse_url()
        response = self.client.post(api_url)
        self.assertEqual(
            response.status_code,
            401
        )

    def test_jwt_login(self):
        print(self.get_jwt_access_token())
