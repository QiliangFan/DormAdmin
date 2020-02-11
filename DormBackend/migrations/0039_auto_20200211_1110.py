# Generated by Django 2.1.12 on 2020-02-11 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DormBackend', '0038_auto_20200211_1105'),
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
        migrations.AlterField(
            model_name='warning',
            name='sponsor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DormBackend.Teacher'),
        ),
    ]
