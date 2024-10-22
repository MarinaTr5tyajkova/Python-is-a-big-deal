# Generated by Django 5.1.1 on 2024-10-01 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='advuser',
            name='send_message',
        ),
        migrations.AddField(
            model_name='advuser',
            name='send_message',
            field=models.BooleanField(default=True, verbose_name='Notify on new comments?'),
        ),
        migrations.AlterField(
            model_name='advuser',
            name='is_activated',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Activated?'),
        ),
    ]
