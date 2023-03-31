# Generated by Django 4.0.4 on 2022-05-13 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('otp', models.IntegerField()),
            ],
            options={
                'db_table': 'visitors',
            },
        ),
        migrations.AddField(
            model_name='dishes',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant.category'),
            preserve_default=False,
        ),
    ]