import django_filters
from django.core.mail import send_mail
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from rental import models, serializers
from rental.permissions import IsOwner


class FriendViewset(NestedViewSetMixin, viewsets.ModelViewSet):
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


class BorrowedViewset(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer

    # filter using django_filters
    # filterset_fields = {
    #     'returned': ['exact', 'lte', 'gte', 'isnull']
    # }

    # My own filterSet
    filterset_class = BorrowedFilterSet

    @action(detail=True, url_path='remind', methods=['post'])
    def remind_single(self, request, *args, **kwargs):
        obj = self.get_object()
        send_mail(
            subject=f"Please return my belonging: {obj.what.name}",
            message=f'You forgot to return my belonging: "{obj.what.name}"" that you borrowed on {obj.when}. Please return it.',
            from_email="teste@email.com",
            recipient_list=[obj.to_who.email],
            fail_silently=False
        )
        return Response("Email sent.")
