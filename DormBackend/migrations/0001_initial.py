# Generated by Django 2.1.12 on 2020-02-11 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InspectionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2020)),
                ('month', models.IntegerField(default=1)),
                ('day', models.IntegerField(default=1)),
                ('date', models.DateTimeField(auto_now=True)),
                ('result', models.CharField(default='', max_length=32, null=True)),
                ('comment', models.CharField(default='', max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pwd', models.CharField(default='123456', max_length=32)),
                ('level', models.IntegerField(default='1')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(default='', max_length=32, null=True)),
                ('build', models.CharField(default='', max_length=32, null=True)),
                ('capacity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StuAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pwd', models.CharField(default='123456', max_length=32)),
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
                ('detail', models.CharField(default='', max_length=32, null=True)),
                ('home_address', models.TextField(default='', null=True)),
                ('name', models.CharField(default='', max_length=32, null=True)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DormBackend.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tea_id', models.CharField(default='', max_length=32, null=True)),
                ('name', models.CharField(default='', max_length=16, null=True)),
                ('college', models.CharField(default='', max_length=32, null=True)),
                ('tel', models.CharField(default='', max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Warning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(default='', max_length=32, null=True)),
                ('comment', models.CharField(default='', max_length=512, null=True)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DormBackend.Room')),
                ('sponsor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DormBackend.Teacher')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DormBackend.Teacher'),
        ),
        migrations.AddField(
            model_name='stuaccount',
            name='account_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DormBackend.Student'),
        ),
        migrations.AddField(
            model_name='manageraccount',
            name='account_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DormBackend.Teacher'),
        ),
        migrations.AddField(
            model_name='inspectionhistory',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DormBackend.Room'),
        ),
    ]
