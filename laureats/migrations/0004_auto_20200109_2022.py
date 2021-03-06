# Generated by Django 3.0.2 on 2020-01-09 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laureats', '0003_auto_20200109_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='laureat',
            name='promotion',
            field=models.ForeignKey(default=2019, on_delete=django.db.models.deletion.CASCADE, related_name='laureats', to='laureats.Promotion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='promotion',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
