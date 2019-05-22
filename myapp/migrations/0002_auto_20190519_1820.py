# Generated by Django 2.2.1 on 2019-05-19 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='warehouse',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(default='Windsor', max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_units', models.PositiveIntegerField(default=1)),
                ('order_status', models.IntegerField(choices=[(0, 'Order Cancelled'), (1, 'Order Placed'), (2, 'Order Shipped'), (3, 'Oder Delivered')])),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='client', to='myapp.Client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='product', to='myapp.Product')),
            ],
        ),
    ]