# Generated by Django 4.1 on 2022-08-10 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meals', models.CharField(choices=[('P', 'Potion'), ('SP', 'Super Potion'), ('HP', 'Hyper Potion'), ('RC', 'Rare Candy'), ('R', 'Revive')], max_length=2, verbose_name='Item Given')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.pokemon')),
            ],
        ),
    ]