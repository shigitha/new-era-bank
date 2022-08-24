# Generated by Django 4.1 on 2022-08-23 20:20

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'dictrict',
                'verbose_name_plural': 'districts',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('DOB', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=10)),
                ('phone_number', models.CharField(max_length=80, unique=True)),
                ('mail_id', models.EmailField(max_length=250)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('address3', models.CharField(max_length=200)),
                ('materialprovide', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credentials.account')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credentials.branch')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credentials.district')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credentials.district'),
        ),
    ]
