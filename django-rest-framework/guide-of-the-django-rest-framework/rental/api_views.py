import pendulum
from rest_framework import viewsets

from rental import models, serializers
from rental.permissions import IsOwner


class FriendViewset(viewsets.ModelViewSet):
    queryset = models.Friend.objects.with_overdue()
    serializer_class = serializers.FriendSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return super().get_queryset().annotate(
            ann_overdue=models.Case(
                models.When(
                    borrowed__when__lte=pendulum.now().subtract(months=2),
                    then=True),
                default=models.Value(False),
                output_field=models.BooleanField()
            )
        )


class BelongingViewset(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer


class BorrowedViewset(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer
