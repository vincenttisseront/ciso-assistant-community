# Generated by Django 5.0.4 on 2024-07-22 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_requirementassessment_mapping_inference_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='framework',
            name='translations',
            field=models.JSONField(blank=True, null=True, verbose_name='Translations'),
        ),
        migrations.AddField(
            model_name='loadedlibrary',
            name='translations',
            field=models.JSONField(blank=True, null=True, verbose_name='Translations'),
        ),
        migrations.AddField(
            model_name='referencecontrol',
            name='translations',
            field=models.JSONField(blank=True, null=True, verbose_name='Translations'),
        ),
        migrations.AddField(
            model_name='requirementmappingset',
            name='translations',
            field=models.JSONField(blank=True, null=True, verbose_name='Translations'),
        ),
        migrations.AddField(
            model_name='requirementnode',
            name='translations',
            field=models.JSONField(blank=True, null=True, verbose_name='Translations'),
        ),
        migrations.AddField(
            model_name='riskmatrix',
            name='translations',
            field=models.JSONField(blank=True, null=True, verbose_name='Translations'),
        ),
        migrations.AddField(
            model_name='storedlibrary',
            name='translations',
            field=models.JSONField(blank=True, null=True, verbose_name='Translations'),
        ),
        migrations.AddField(
            model_name='threat',
            name='translations',
            field=models.JSONField(blank=True, null=True, verbose_name='Translations'),
        ),
    ]
