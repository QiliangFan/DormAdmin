# Generated by Django 2.1.12 on 2020-02-10 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DormBackend', '0007_auto_20200210_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manageraccount',
            name='account_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DormBackend.Teacher'),
        ),
        migrations.AlterField(
            model_name='student',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DormBackend.Teacher'),
        ),
    ]
