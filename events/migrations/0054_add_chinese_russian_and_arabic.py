# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-17 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0053_allow_null_place_info_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description_ar',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='event',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='event',
            name='description_zh',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='event',
            name='headline_ar',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Headline'),
        ),
        migrations.AddField(
            model_name='event',
            name='headline_ru',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Headline'),
        ),
        migrations.AddField(
            model_name='event',
            name='headline_zh',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Headline'),
        ),
        migrations.AddField(
            model_name='event',
            name='info_url_ar',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='Event home page'),
        ),
        migrations.AddField(
            model_name='event',
            name='info_url_ru',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='Event home page'),
        ),
        migrations.AddField(
            model_name='event',
            name='info_url_zh',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='Event home page'),
        ),
        migrations.AddField(
            model_name='event',
            name='location_extra_info_ar',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Location extra info'),
        ),
        migrations.AddField(
            model_name='event',
            name='location_extra_info_ru',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Location extra info'),
        ),
        migrations.AddField(
            model_name='event',
            name='location_extra_info_zh',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Location extra info'),
        ),
        migrations.AddField(
            model_name='event',
            name='name_ar',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='event',
            name='name_ru',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='event',
            name='name_zh',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='event',
            name='provider_ar',
            field=models.CharField(max_length=512, null=True, verbose_name='Provider'),
        ),
        migrations.AddField(
            model_name='event',
            name='provider_ru',
            field=models.CharField(max_length=512, null=True, verbose_name='Provider'),
        ),
        migrations.AddField(
            model_name='event',
            name='provider_zh',
            field=models.CharField(max_length=512, null=True, verbose_name='Provider'),
        ),
        migrations.AddField(
            model_name='event',
            name='secondary_headline_ar',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Secondary headline'),
        ),
        migrations.AddField(
            model_name='event',
            name='secondary_headline_ru',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Secondary headline'),
        ),
        migrations.AddField(
            model_name='event',
            name='secondary_headline_zh',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Secondary headline'),
        ),
        migrations.AddField(
            model_name='event',
            name='short_description_ar',
            field=models.TextField(blank=True, null=True, verbose_name='Short description'),
        ),
        migrations.AddField(
            model_name='event',
            name='short_description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Short description'),
        ),
        migrations.AddField(
            model_name='event',
            name='short_description_zh',
            field=models.TextField(blank=True, null=True, verbose_name='Short description'),
        ),
        migrations.AddField(
            model_name='keyword',
            name='name_ar',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='keyword',
            name='name_ru',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='keyword',
            name='name_zh',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='keywordset',
            name='name_ar',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='keywordset',
            name='name_ru',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='keywordset',
            name='name_zh',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='language',
            name='name_ar',
            field=models.CharField(max_length=20, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='language',
            name='name_ru',
            field=models.CharField(max_length=20, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='language',
            name='name_zh',
            field=models.CharField(max_length=20, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='license',
            name='name_ar',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='license',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='license',
            name='name_zh',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='offer',
            name='description_ar',
            field=models.TextField(blank=True, null=True, verbose_name='Offer description'),
        ),
        migrations.AddField(
            model_name='offer',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Offer description'),
        ),
        migrations.AddField(
            model_name='offer',
            name='description_zh',
            field=models.TextField(blank=True, null=True, verbose_name='Offer description'),
        ),
        migrations.AddField(
            model_name='offer',
            name='info_url_ar',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='Web link to offer'),
        ),
        migrations.AddField(
            model_name='offer',
            name='info_url_ru',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='Web link to offer'),
        ),
        migrations.AddField(
            model_name='offer',
            name='info_url_zh',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='Web link to offer'),
        ),
        migrations.AddField(
            model_name='offer',
            name='price_ar',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='offer',
            name='price_ru',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='offer',
            name='price_zh',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='place',
            name='address_locality_ar',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address locality'),
        ),
        migrations.AddField(
            model_name='place',
            name='address_locality_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address locality'),
        ),
        migrations.AddField(
            model_name='place',
            name='address_locality_zh',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address locality'),
        ),
        migrations.AddField(
            model_name='place',
            name='description_ar',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='place',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='place',
            name='description_zh',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='place',
            name='info_url_ar',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='Place home page'),
        ),
        migrations.AddField(
            model_name='place',
            name='info_url_ru',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='Place home page'),
        ),
        migrations.AddField(
            model_name='place',
            name='info_url_zh',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='Place home page'),
        ),
        migrations.AddField(
            model_name='place',
            name='name_ar',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='place',
            name='name_ru',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='place',
            name='name_zh',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='place',
            name='street_address_ar',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Street address'),
        ),
        migrations.AddField(
            model_name='place',
            name='street_address_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Street address'),
        ),
        migrations.AddField(
            model_name='place',
            name='street_address_zh',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Street address'),
        ),
        migrations.AddField(
            model_name='place',
            name='telephone_ar',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Telephone'),
        ),
        migrations.AddField(
            model_name='place',
            name='telephone_ru',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Telephone'),
        ),
        migrations.AddField(
            model_name='place',
            name='telephone_zh',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Telephone'),
        ),
    ]
