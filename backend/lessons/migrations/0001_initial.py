# Generated by Django 4.1.3 on 2022-11-16 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание модуля')),
            ],
            options={
                'verbose_name': 'модуль',
                'verbose_name_plural': 'модули',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание урока')),
                ('document_url', models.URLField(max_length=128, verbose_name='ссылка на документ')),
                ('homework_url', models.URLField(max_length=128, verbose_name='ссылка на домашнее задание')),
                ('order_number', models.PositiveIntegerField(verbose_name='порядок урока в модуле')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lessons', to='lessons.module', verbose_name='модуль')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
                'ordering': ['module', 'order_number'],
            },
        ),
        migrations.AddConstraint(
            model_name='lesson',
            constraint=models.UniqueConstraint(fields=('module_id', 'order_number'), name='unique_module_order'),
        ),
    ]