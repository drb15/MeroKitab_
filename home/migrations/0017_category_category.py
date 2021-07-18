# Generated by Django 3.0.6 on 2021-07-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('Engineering', 'Engineering'), ('Science', 'Science'), ('Management', 'Management'), ('Literature', 'Literature'), ('Arts', 'Arts'), ('School', 'School Level'), ('Religion', 'Religion'), ('Law', 'Law'), ('Entrance', 'Entrance Preparation'), ('Government', 'Government Jobs'), ('Miscellenous', 'Miscelleneous')], default='Miscellenous', max_length=100),
        ),
    ]
