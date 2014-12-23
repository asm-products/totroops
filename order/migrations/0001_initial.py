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
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('source', models.TextField()),
                ('cost', models.FloatField()),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('length', models.FloatField()),
                ('width', models.FloatField()),
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
                ('message', models.TextField(max_length=500, blank=True)),
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
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('length', models.FloatField()),
                ('width', models.FloatField()),
                ('container', models.TextField()),
                ('shipping', models.FloatField()),
                ('price', models.FloatField()),
                ('tax', models.FloatField()),
                ('items', models.ManyToManyField(to='order.Item')),
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
            field=models.ManyToManyField(to='order.Package'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='recipient',
            field=models.ForeignKey(to='order.Recipient'),
            preserve_default=True,
        ),
    ]
