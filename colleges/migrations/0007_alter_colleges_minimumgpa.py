# Generated by Django 3.2.9 on 2022-03-11 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0006_alter_colleges_additionalinformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colleges',
            name='MinimumGpa',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]