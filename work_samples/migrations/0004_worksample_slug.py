# Generated by Django 4.2.5 on 2023-09-18 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_samples', '0003_worksampletag_worksample_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksample',
            name='slug',
            field=models.SlugField(default='test', unique=True),
            preserve_default=False,
        ),
    ]
