# Generated by Django 4.2.16 on 2024-09-26 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_comment_com_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='com_to_pub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.publication'),
        ),
    ]
