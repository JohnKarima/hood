# Generated by Django 3.1.2 on 2020-10-31 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0002_business_neighbourhood_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='biz_digits',
            field=models.IntegerField(null=True),
        ),
    ]
