from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from rental import models


class FriendSerializer(FlexFieldsModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = models.Friend
        fields = ('id', 'name', "owner", 'has_overdue')


class BelongingSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Belonging
        fields = ('id', 'name')


class BorrowedSerializer(FlexFieldsModelSerializer):
    expandable_fields = {
        "what": (BelongingSerializer),
        "to_who": (FriendSerializer),
    }

    class Meta:
        model = models.Borrowed
        fields = ('id', 'what', 'to_who', 'when', 'returned')
