from django.db import models


class TestModel(models.Model):
    string = models.CharField(max_length=20, verbose_name='name of field one')
    date = models.DateField(verbose_name='Date one')
    datetime = models.DateTimeField(verbose_name='Date and Time')
    check_point = models.BooleanField(verbose_name='Check point')
    integer = models.IntegerField(verbose_name='Number')
    choice = models.IntegerField(verbose_name='Choice', choices=(
        (1, 'one'),
        (2, 'two'),
        (3, 'three'),
        (4, 'four')
    ))
    nullable = models.TextField(verbose_name='Null text', blank=True)

    def __str__(self):
        return f'Test model №{self.id}'
