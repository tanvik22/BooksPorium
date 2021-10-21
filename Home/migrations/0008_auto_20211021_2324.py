# Generated by Django 3.1.7 on 2021-10-21 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_books',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='upload_books',
            name='book_file',
            field=models.FileField(default='', upload_to='./static/Material/'),
        ),
    ]
