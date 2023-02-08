from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tag.models import Tag

from ..models import Recipe
from ..serializers import RecipeSerializer, TagSerializer


class RecipeAPIv2Pagination(PageNumberPagination):
    page_size = 2


class RecipeAPIv2ViewSet(ModelViewSet):
    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv2Pagination
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teste"] = "exaple"
        return context

    def get_queryset(self):
        qs = super().get_queryset()

        category_id = self.request.query_params.get('category_id', None)

        if category_id != '' and category_id is not None and category_id.isnumeric():
            qs = qs.filter(category_id=category_id)

        return qs

    # Overwrite partial_update from django rest framework

    def partial_update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        recipe = self.get_queryset().filter(pk=pk).first()
        serializer = RecipeSerializer(
            instance=recipe,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,)


# class RecipeAPIv2List(ListCreateAPIView):
#     queryset = Recipe.objects.get_published()
#     serializer_class = RecipeSerializer
#     pagination_class = RecipeAPIv2Pagination
#     # def get(self, request):
#     #     recipes = Recipe.objects.get_published()[:10]
#     #     serializer = RecipeSerializer(
#     #         instance=recipes, many=True, context={'request': request})
#     #     return Response(serializer.data)

#     # def post(self, request):
#     #     serializer = RecipeSerializer(data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save()
#     #     return Response(
#     #         serializer.data,
#     #         status=status.HTTP_201_CREATED
#     #     )


# class RecipeAPIv2Detail(RetrieveUpdateDestroyAPIView):
#     queryset = Recipe.objects.get_published()
#     serializer_class = RecipeSerializer
#     pagination_class = RecipeAPIv2Pagination

#     # Overwrite partial_update from django rest framework
#     def partial_update(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         recipe = self.get_queryset().filter(pk=pk).first()
#         serializer = RecipeSerializer(
#             instance=recipe,
#             data=request.data,
#             many=False,
#             context={'request': request},
#             partial=True
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,)


@api_view()
def tag_api_detail(request, pk):
    tag = get_object_or_404(
        Tag.objects.all(),
        pk=pk,
    )
    serializer = TagSerializer(
        instance=tag,
        many=False,
    )
    return Response(serializer.data)
