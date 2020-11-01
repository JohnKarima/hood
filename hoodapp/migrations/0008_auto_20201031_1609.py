# Generated by Django 3.1.2 on 2020-10-31 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0007_auto_20201031_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='prof_ref',
        ),
        migrations.AddField(
            model_name='profile',
            name='hood_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='hoodapp.neighbourhood'),
        ),
    ]