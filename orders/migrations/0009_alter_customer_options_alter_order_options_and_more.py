# Generated by Django 4.2.3 on 2024-03-29 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_shiping_price_shiping_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': 'کاربر ها'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'سفارشات'},
        ),
        migrations.AlterModelOptions(
            name='province',
            options={'verbose_name_plural': 'استان ها'},
        ),
        migrations.AlterModelOptions(
            name='shiping_price',
            options={'verbose_name': 'تغییر هزینه پست و بسته بندی'},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='birht_date',
        ),
    ]
