from django.db import models

SIZE_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
)

TYPE_CHOICES = (
    ('S', 'Standard'),
    ('T', 'Thin'),
    ('P', 'Philadelphia'),
    ('H', 'Hot-Dog Crust')
)


class Ingredient(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']


class Dish(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    size = models.CharField(choices=SIZE_CHOICES, default='S', max_length=100)
    type = models.CharField(choices=TYPE_CHOICES, default='S', max_length=100)
    ingredients = models.ManyToManyField('Ingredient', related_name='dishes_list', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
