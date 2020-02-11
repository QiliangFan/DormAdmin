# Generated by Django 2.1.12 on 2020-02-10 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pwd', models.CharField(default='123456', max_length=32)),
                ('level', models.IntegerField(default='1', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(default='', max_length=32, null=True)),
                ('build', models.CharField(default='', max_length=32, null=True)),
                ('result', models.CharField(default='', max_length=32, null=True)),
                ('comment', models.CharField(default='', max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.CharField(default='', max_length=32, null=True)),
                ('emergence_tel', models.CharField(default='', max_length=16, null=True)),
                ('tel', models.CharField(default='', max_length=16, null=True)),
                ('college', models.CharField(default='', max_length=32, null=True)),
                ('major', models.CharField(default='', max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tea_id', models.CharField(default='', max_length=32, null=True)),
                ('name', models.CharField(default='', max_length=16, null=True)),
                ('college', models.CharField(default='', max_length=32, null=True)),
                ('tel', models.CharField(default='', max_length=16, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DormBackend.Teacher'),
        ),
        migrations.AddField(
            model_name='account',
            name='account_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DormBackend.Teacher'),
        ),
    ]
