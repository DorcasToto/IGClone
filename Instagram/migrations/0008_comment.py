# Generated by Django 3.1.3 on 2020-11-21 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0007_auto_20201121_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('postt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Instagram.image')),
                ('userr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Instagram.profile')),
            ],
        ),
    ]
