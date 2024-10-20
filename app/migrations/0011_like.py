# Generated by Django 4.2.16 on 2024-10-15 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_rename_coor_adres_coordinate_coor_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_bool', models.BooleanField(default=False)),
                ('like_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('like_to_pub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='app.publication')),
            ],
        ),
    ]
