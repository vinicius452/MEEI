# Generated by Django 4.2.6 on 2023-11-21 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depoimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150)),
                ('nome', models.CharField(max_length=150)),
                ('depoimento_ou_discussao', models.CharField(choices=[('depoimento', 'Depoimento'), ('discussao', 'Discussão')], max_length=11)),
                ('relato', models.TextField()),
            ],
        ),
    ]