# Generated by Django 3.0 on 2020-03-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sphere', '0002_auto_20200313_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courcemodel',
            name='cource_photo',
            field=models.ImageField(default='', upload_to='static/cource'),
        ),
    ]
