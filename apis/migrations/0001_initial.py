# Generated by Django 2.0.9 on 2018-10-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=250)),
                ('done', models.BooleanField()),
                ('priority', models.CharField(choices=[('H', 'high'), ('M', 'middle'), ('L', 'low')], default='L', max_length=1)),
            ],
        ),
    ]