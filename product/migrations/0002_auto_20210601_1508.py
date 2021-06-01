# Generated by Django 3.2.3 on 2021-06-01 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_voted']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_posted']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='pub_date',
            new_name='date_posted',
        ),
        migrations.AddField(
            model_name='comment',
            name='date_voted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]