from tortoise import Model, fields


class BaseModel(Model):
    class Meta:
        abstract = True


class TimeBasedModel(BaseModel):
    class Meta:
        abstract = True

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
