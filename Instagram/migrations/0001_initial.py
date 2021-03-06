# Generated by Django 3.1.3 on 2020-11-20 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilephoto', models.ImageField(upload_to='images')),
                ('Bio', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('imageName', models.CharField(max_length=30)),
                ('imageCaption', models.CharField(max_length=30)),
                ('likes', models.IntegerField()),
                ('comments', models.CharField(max_length=30)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Instagram.profile')),
            ],
        ),
    ]
