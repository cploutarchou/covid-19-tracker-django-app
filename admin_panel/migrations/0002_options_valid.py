from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('admin_panel_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='options',
            name='valid',
            field=models.BooleanField(default=True, verbose_name='Valid'),
        ),
    ]
