# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('vorname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Raum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nummer', models.CharField(unique=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unterrichtsfach', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Unterrichtsplan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jahrgang', models.IntegerField()),
                ('kurs', models.CharField(max_length=15)),
                ('tag', models.IntegerField(choices=[(1, b'Mo'), (2, b'Di'), (3, b'Mi'), (4, b'Do'), (5, b'Fr')])),
                ('std', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('Unterrict', models.ForeignKey(to='stundenplan.Subject')),
                ('raum', models.ForeignKey(to='stundenplan.Raum')),
            ],
        ),
        migrations.CreateModel(
            name='Lehrer',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='stundenplan.Person')),
                ('facher', models.ManyToManyField(to='stundenplan.Subject')),
            ],
            bases=('stundenplan.person',),
        ),
        migrations.CreateModel(
            name='Schueler',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='stundenplan.Person')),
                ('jahrgang', models.IntegerField()),
                ('klasse', models.CharField(max_length=5)),
            ],
            bases=('stundenplan.person',),
        ),
        migrations.AddField(
            model_name='unterrichtsplan',
            name='lehrer',
            field=models.ForeignKey(to='stundenplan.Lehrer'),
        ),
        migrations.AddField(
            model_name='unterrichtsplan',
            name='personas',
            field=models.ManyToManyField(to='stundenplan.Schueler'),
        ),
    ]
