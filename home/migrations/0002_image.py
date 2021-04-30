# Generated by Django 3.1.7 on 2021-04-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
                ('name', models.CharField(default='', max_length=100)),
                ('org', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('pin', models.IntegerField(default='')),
                ('hog', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(upload_to='img/%y')),
            ],
        ),
    ]
