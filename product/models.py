from django.db import models


# class Product(models.Model):
#     title = models.CharField(max_length=255, verbose_name="Product Name")
#     text = models.TextField(null=True, blank=True, verbose_name="Description")
#     rate = models.FloatField(default=0, verbose_name="Popularity")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
#     updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
#     image = models.ImageField(
#         upload_to='products', null=True, blank=False,
#         verbose_name="Photo"
#     )
#
#     def __str__(self) -> str:
#         return f"{self.title} {self.rate}"
#
#     class Meta:
#         db_table = 'product'
#         verbose_name = 'Product'
#         verbose_name_plural = 'Products'

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
        db_table = 'Categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(BaseModel):
    image = models.ImageField(
        upload_to='posts',
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
        related_name="Products"
    )

    def __str__(self) -> str:
        return f"{self.title} {self.rate}"

    class Meta:
        db_table = 'Products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
