# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-27 16:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0003_auto_20171127_1409'),
        ('core', '0002_auto_20171127_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('usuario_id', models.OneToOneField(db_column='usuario_id', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='core.Curso')),
            ],
            options={
                'abstract': False,
            },
            bases=('Auth.usuario',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('usuario_id', models.OneToOneField(db_column='usuario_id', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telefone', models.CharField(blank=True, max_length=11, null=True)),
            ],
            options={
                'verbose_name_plural': 'professores',
            },
            bases=('Auth.usuario',),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Aluno'),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Aluno'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Professor'),
        ),
    ]
