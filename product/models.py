from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Category Name")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Review(BaseModel):
    # text = models.CharField(max_length=255, verbose_name="Some Review")
    product = models.ForeignKey(
        "product.Review",  # Поле для связи с другой моделью
        on_delete=models.CASCADE,
        # Политика удаления записи в связанной модели (CASCADE - удалить все записи, которые связаны с этой записью)
        verbose_name="Review",  # Название поля в форме (админка, форма регистрации, форма авторизации)
        related_name="reviews"  # Поле для обратной связи (по умолчанию appname_classname_set (post_comments_set))
    )
    text = models.TextField(null=True, blank=True, verbose_name="Some Review")  # Поле для ввода текста без ограничения

    def __str__(self) -> str:
        return f"{self.text}"

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class Product(BaseModel):
    image = models.ImageField(
        upload_to='products',
        null=True,
        blank=False,
        verbose_name="Фото")
    title = models.CharField(max_length=255,
                             verbose_name="Product Name")
    text = models.TextField(null=True, blank=True, verbose_name="Description")
    rate = models.FloatField(default=0, verbose_name="Popularity")
    hashtags = models.ManyToManyField(
        Category,
        verbose_name="Categories",
        related_name="products"
    )
    def __str__(self) -> str:
        return f"{self.title} {self.rate}"

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
