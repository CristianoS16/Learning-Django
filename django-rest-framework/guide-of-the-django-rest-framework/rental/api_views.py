import django_filters
from rest_framework import viewsets

from rental import models, serializers
from rental.permissions import IsOwner


class FriendViewset(viewsets.ModelViewSet):
    queryset = models.Friend.objects.with_overdue()
    serializer_class = serializers.FriendSerializer
    permission_classes = [IsOwner]


class BelongingViewset(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer

    # My own filterSet


class BorrowedFilterSet(django_filters.FilterSet):
    missing = django_filters.BooleanFilter(
        field_name='returned', lookup_expr='isnull')
    overdue = django_filters.BooleanFilter(
        method="get_overdue", field_name="returned")

    class Meta:
        model = models.Borrowed
        fields = ["what", "to_who", "missing", "overdue"]

    def get_overdue(self, queryset, field_name, value):
        if value:
            return queryset.overdue()
        return queryset


class BorrowedViewset(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer

    # filter using django_filters
    # filterset_fields = {
    #     'returned': ['exact', 'lte', 'gte', 'isnull']
    # }

    # My own filterSet
    filterset_class = BorrowedFilterSet
