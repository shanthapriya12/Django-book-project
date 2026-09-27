from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=200)

    author = models.CharField(max_length=100)

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books'
    )

    cover = models.ImageField(
        upload_to='books/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.title} by {self.author} - ${self.price}"