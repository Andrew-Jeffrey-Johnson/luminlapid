from django.db import migrations, models

def split_name(apps, schema_editor):
    User = apps.get_model('users', 'User')
    for user in User.objects.all():
        # Assuming the name is in the format "First Middle Last"
        parts = user.name.split()
        user.first_name = parts[0]
        user.middle_name = parts[1] if len(parts) > 2 else ''
        user.last_name = parts[-1]
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='middle_name',
            field=models.CharField(max_length=255, blank=True, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=255, default=''),
        ),
        migrations.RunPython(split_name),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]