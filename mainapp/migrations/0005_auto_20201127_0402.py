# Generated by Django 3.1.3 on 2020-11-27 04:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_delete_somemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='sd_volume',
        ),
        migrations.AddField(
            model_name='cart',
            name='for_anonymous_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='in_order',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='sd_volume_max',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Максимальный объем встраивамой памяти'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Общая цена'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.customer', verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='processor_freq',
            field=models.CharField(max_length=255, verbose_name='Частота процессора'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='accum_volume',
            field=models.CharField(max_length=255, verbose_name='Объем батареи'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='resolution',
            field=models.CharField(max_length=255, verbose_name='Разрешение экрана'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='sd',
            field=models.BooleanField(default=True, verbose_name='Наличие SD карты'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Наименование'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адрес')),
                ('status', models.CharField(choices=[('new', 'Новый заказ'), ('in_progress', 'Заказ в обработке'), ('is_ready', 'Заказ готов'), ('completed', 'Заказ выполнен')], default='new', max_length=100, verbose_name='Статус заказ')),
                ('buying_type', models.CharField(choices=[('self', 'Самовывоз'), ('delivery', 'Доставка')], default='self', max_length=100, verbose_name='Тип заказа')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')),
                ('order_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата получения заказа')),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.cart', verbose_name='Корзина')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_orders', to='mainapp.customer', verbose_name='Покупатель')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='related_order', to='mainapp.Order', verbose_name='Заказы покупателя'),
        ),
    ]
