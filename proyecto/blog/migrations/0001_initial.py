# Generated by Django 4.2.6 on 2023-11-06 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('post', models.CharField(max_length=256)),
                ('signature', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Temas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('creador', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_nac', models.DateField(null=True)),
                ('dni', models.CharField(max_length=20)),
                ('telefono', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
