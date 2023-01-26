from django.contrib.auth.models import User
from rest_framework import serializers

from tag.models import Tag

from .models import Category, Recipe


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name']


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'author', 'category', 'category_name',
                  'tags', 'public', 'preparation', 'tag_objects', 'tag_links']

    public = serializers.BooleanField(source="is_published", read_only=True)
    preparation = serializers.SerializerMethodField(
        method_name="any_method_name", read_only=True)
    # category = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all(),
    # )
    category_name = serializers.StringRelatedField(
        source='category',
        read_only=True
    )
    tag_objects = TagSerializer(many=True, source="tags", read_only=True)
    tag_links = serializers.HyperlinkedRelatedField(
        many=True,
        source='tags',
        view_name='recipes:recipe_api_v2_tag',
        read_only=True
    )

    def any_method_name(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
