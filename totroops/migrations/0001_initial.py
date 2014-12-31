# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=50)),
                ('discount', models.FloatField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True, blank=True)),
                ('valid', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('source', models.TextField()),
                ('cost', models.FloatField()),
                ('weight', models.FloatField(null=True, blank=True)),
                ('height', models.FloatField(null=True, blank=True)),
                ('length', models.FloatField(null=True, blank=True)),
                ('width', models.FloatField(null=True, blank=True)),
                ('food', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(max_length=500, null=True, blank=True)),
                ('image_url', models.CharField(max_length=1000, null=True, blank=True)),
                ('coupon', models.ForeignKey(blank=True, to='totroops.Coupon', null=True)),
                ('customer', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cost', models.FloatField()),
                ('weight', models.FloatField(null=True, blank=True)),
                ('height', models.FloatField(null=True, blank=True)),
                ('length', models.FloatField(null=True, blank=True)),
                ('width', models.FloatField(null=True, blank=True)),
                ('container', models.TextField()),
                ('shipping', models.FloatField()),
                ('price', models.FloatField()),
                ('tax', models.FloatField()),
                ('items', models.ManyToManyField(to='totroops.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('address', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='packages',
            field=models.ManyToManyField(to='totroops.Package'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='recipient',
            field=models.ForeignKey(to='totroops.Recipient'),
            preserve_default=True,
        ),
    ]
