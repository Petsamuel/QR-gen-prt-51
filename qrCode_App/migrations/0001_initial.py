# Generated by Django 4.0.6 on 2022-08-07 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import qrCode_App.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QrCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_type', models.CharField(max_length=100)),
                ('qr_code_text', models.TextField()),
                ('qr_msg', models.TextField(null=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to=qrCode_App.models.get_upload_path)),
                ('qr_code_date', models.DateField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]