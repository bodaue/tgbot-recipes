from tortoise import fields

from tgbot.db.models.base import BaseModel


class RecipeCategory(BaseModel):
    class Meta:
        table = "recipe_categories"

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Recipe(BaseModel):
    class Meta:
        table = "recipes"

    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255, unique=True)
    description = fields.TextField()
    ingredients = fields.TextField()
    preparation_time = fields.TimeDeltaField()
    category = fields.ForeignKeyField("models.RecipeCategory",
                                      related_name="recipes")

    def get_details(self) -> str:
        hours, remainder = divmod(self.preparation_time.total_seconds(), 3600)
        minutes = remainder // 60
        preparation_time_str = f"{int(hours)} ч {int(minutes)} мин" if hours else f"{int(minutes)} мин"
        return (
            f"<b>Рецепт:</b> {self.title}\n"
            f"{self.description}\n\n"
            f""
            f"<b>Ингредиенты:</b>\n"
            f"{self.ingredients}\n\n"
            f""
            f"<i>Время приготовления:</i> {preparation_time_str}"
        )