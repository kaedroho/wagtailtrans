# Generated by Django 2.1.7 on 2019-02-18 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailtrans', '0007_auto_20180327_1127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['position'], 'verbose_name': 'Language', 'verbose_name_plural': 'Languages'},
        ),
        migrations.AlterModelOptions(
            name='translatablepage',
            options={'verbose_name': 'Translatable page', 'verbose_name_plural': 'Translatable pages'},
        ),
        migrations.RenameField(
            model_name='translatablepage',
            old_name='canonical_page',
            new_name='canonical',
        ),
    ]
