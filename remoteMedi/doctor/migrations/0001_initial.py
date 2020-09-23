# Generated by Django 3.1 on 2020-09-21 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=10)),
                ('contact', models.CharField(default='010-0000-0000', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.major')),
            ],
            options={
                'verbose_name_plural': 'doctor',
                'ordering': ['created_at'],
            },
        ),
    ]