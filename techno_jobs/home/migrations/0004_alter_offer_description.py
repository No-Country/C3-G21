# Generated by Django 4.1.dev20220219193601 on 2022-03-10 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_offer_company_offer_description_offer_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.CharField(max_length=2000, verbose_name='Descripción'),
        ),
    ]
