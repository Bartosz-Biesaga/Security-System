# Generated by Django 4.2 on 2024-12-12 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='building',
            old_name='company_id',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='zone',
            old_name='building_id',
            new_name='building',
        ),
        migrations.AddField(
            model_name='zone',
            name='label',
            field=models.CharField(default='aaa', max_length=255),
            preserve_default=False,
        ),
    ]
