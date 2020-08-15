from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('admin_panel_settings', '0004_auto_20190708_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='priority_level',
            field=models.IntegerField(default=100, verbose_name='Priority Level'),
        ),
    ]
