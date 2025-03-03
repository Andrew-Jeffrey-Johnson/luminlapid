from django.db import migrations, models
from phonenumber_field.modelfields import PhoneNumberField
import datetime

def backfill_joined_dates(apps, schema_editor):
    User = apps.get_model('users', 'User')
    for user in User.objects.all():
        # All users are now joining
        user.joined_date = datetime.datetime.now()
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_split_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=PhoneNumberField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='joined_date',
            field=models.DateField(default=datetime.datetime.now()),
        ),
        migrations.RunPython(backfill_joined_dates),
    ]