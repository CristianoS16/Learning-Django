import pendulum
from rest_framework import serializers

from rental import models


class FriendSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    has_overdue = serializers.SerializerMethodField()

    class Meta:
        model = models.Friend
        fields = ('id', 'name', 'has_overdue')

    def get_has_overdue(self, obj):
        if hasattr(obj, 'ann_overdue'):
            return obj.ann_overdue
        return obj.borrowed_set.filter(
            returned__isnull=True, when=pendulum.now().subtract(months=2)
        ).exists()


class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Belonging
        fields = ('id', 'name')


class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Borrowed
        fields = ('id', 'what', 'to_who', 'when', 'returned')
