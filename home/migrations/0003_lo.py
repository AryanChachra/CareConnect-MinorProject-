# Generated by Django 5.0.1 on 2024-02-09 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_address1_registration_address1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='lo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.TextField()),
            ],
        ),
    ]