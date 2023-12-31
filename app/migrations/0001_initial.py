# Generated by Django 4.2.6 on 2023-12-08 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('Author_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Author_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('DEPTNO', models.IntegerField(primary_key=True, serialize=False)),
                ('DNAME', models.CharField(max_length=100)),
                ('LOC', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('EMPNO', models.IntegerField(primary_key=True, serialize=False)),
                ('ENAME', models.CharField(max_length=100)),
                ('JOB', models.CharField(max_length=100)),
                ('MGR', models.IntegerField()),
                ('HIREDATE', models.DateField()),
                ('SAL', models.PositiveIntegerField()),
                ('COMM', models.FloatField()),
                ('DEPTNO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('Book_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Book_name', models.CharField(max_length=100)),
                ('Book_price', models.PositiveIntegerField()),
                ('Author_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.author')),
            ],
        ),
    ]
