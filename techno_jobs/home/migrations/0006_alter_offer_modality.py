# Generated by Django 4.1.dev20220219193601 on 2022-03-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_offer_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='modality',
            field=models.CharField(choices=[('Presencial', 'Presencial'), ('Full - Time', 'Full - Time'), ('Part - Time', 'Part - Time'), ('Remoto', 'Remoto')], max_length=50, verbose_name='Modalidad'),
        ),
    ]
