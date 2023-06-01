from django.db import models
from django.utils import timezone


class CreatedAt(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=True, blank=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class CreditApplication(CreatedAt):
    name = models.CharField(max_length=128, verbose_name='Наименование кредитной заявки')
    contract = models.OneToOneField('Contract', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Кредитная заявка'
        verbose_name_plural = 'Кредитные заявки'


class Contract(CreatedAt):
    name = models.CharField(max_length=128, verbose_name='Наименование контракта')

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'


class Product(CreatedAt):
    name = models.CharField(max_length=128, verbose_name='Наименование товара')
    credit_application = models.ForeignKey(CreditApplication,
                                           on_delete=models.PROTECT,
                                           related_name='products',
                                           )
    producer = models.ForeignKey('Producer', on_delete=models.PROTECT, related_name='producer_products')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Producer(CreatedAt):
    name = models.CharField(max_length=128, verbose_name='Наименование производителя')

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
