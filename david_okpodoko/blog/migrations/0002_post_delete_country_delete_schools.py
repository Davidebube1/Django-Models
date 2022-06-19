# Generated by Django 4.0.5 on 2022-06-19 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Text', models.TextField(max_length=200)),
                ('Created_date', models.DateTimeField(max_length=200)),
                ('Published_date', models.DateTimeField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='country',
        ),
        migrations.DeleteModel(
            name='schools',
        ),
    ]
