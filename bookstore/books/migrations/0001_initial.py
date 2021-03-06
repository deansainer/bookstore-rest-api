# Generated by Django 4.0.5 on 2022-07-11 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=55)),
                ('pages', models.CharField(max_length=5)),
                ('author', models.CharField(max_length=55)),
                ('price', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
    ]
