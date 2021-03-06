# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-27 17:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20171127_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boletim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota1', models.DecimalField(decimal_places=2, max_digits=4)),
                ('nota2', models.DecimalField(decimal_places=2, max_digits=4)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Aluno')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Turma')),
            ],
            options={
                'verbose_name_plural': 'boletins',
            },
        ),
        migrations.AlterModelOptions(
            name='disciplinaofertada',
            options={'verbose_name_plural': 'disciplinas ofertadas'},
        ),
        migrations.AlterModelOptions(
            name='questao',
            options={'verbose_name_plural': 'Questoes'},
        ),
        migrations.AlterUniqueTogether(
            name='boletim',
            unique_together=set([('turma', 'aluno')]),
        ),
    ]
