# Generated by Django 3.0 on 2020-03-23 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sphere', '0006_auto_20200319_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquirymodel',
            old_name='Cource',
            new_name='Course',
        ),
        migrations.RemoveField(
            model_name='enquirymodel',
            name='College',
        ),
        migrations.RemoveField(
            model_name='enquirymodel',
            name='Semester',
        ),
        migrations.AddField(
            model_name='enquirymodel',
            name='Email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='enquirymodel',
            name='Message',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]