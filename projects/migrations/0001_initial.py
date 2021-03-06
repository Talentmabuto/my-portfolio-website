# Generated by Django 2.0.5 on 2018-06-10 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now=True)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('is_live', models.BooleanField(default=False)),
                ('project_title', models.CharField(max_length=250)),
                ('project_description', models.TextField(blank=True)),
                ('project_url', models.URLField(blank=True, null=True)),
                ('last_viewed', models.DateTimeField()),
                ('slug', models.SlugField()),
            ],
        ),
    ]
