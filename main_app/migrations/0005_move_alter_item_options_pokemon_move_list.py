# Generated by Django 4.1 on 2022-08-10 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_item_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('damage', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='pokemon',
            name='move_list',
            field=models.ManyToManyField(to='main_app.move'),
        ),
    ]