# Generated by Django 4.2.3 on 2024-02-07 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvmsapp', '0010_alter_addvisitor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addvisitor',
            name='mobilenumber',
            field=models.CharField(max_length=15),
        ),
    ]
