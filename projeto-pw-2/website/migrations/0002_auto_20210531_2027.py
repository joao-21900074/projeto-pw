# Generated by Django 3.2.3 on 2021-05-31 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizz',
            name='apelido',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizz',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizz',
            name='nome',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
