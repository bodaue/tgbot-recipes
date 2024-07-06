from tortoise import fields

from tgbot.db.models.base import TimeBasedModel


class User(TimeBasedModel):
    class Meta:
        table = "users"

    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=255)
    username = fields.CharField(max_length=255, null=True)
