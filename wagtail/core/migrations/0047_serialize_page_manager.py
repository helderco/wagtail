# Generated by Django 3.0.3 on 2020-02-12 14:34

from django.db import migrations
import wagtail.core.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0046_add_workflow_models'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='page',
            managers=[
                ('objects', wagtail.core.models.PageManager()),
            ],
        ),
    ]
