from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование контракта')),
            ],
            options={
                'verbose_name': 'Контракт',
                'verbose_name_plural': 'Контракты',
            },
        ),
        migrations.CreateModel(
            name='CreditApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование кредитной заявки')),
                ('contract', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.contract')),
            ],
            options={
                'verbose_name': 'Кредитная заявка',
                'verbose_name_plural': 'Кредитные заявки',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование производителя')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование товара')),
                ('credit_application', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='main.creditapplication')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='producer_products', to='main.producer')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
