# Generated by Django 2.1.4 on 2018-12-16 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eveonline', '0007_token_scopes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evecharacter',
            name='character_alt_type',
            field=models.CharField(blank=True, choices=[('super_alt', 'Super Alt'), ('carrier_alt', 'Carrier Alt'), ('dread_alt', 'Dread Alt'), ('fax_alt', 'Fax Alt'), ('rorqual_alt', 'Rorqual Alt'), ('cap_alt', 'Capital Alt'), ('subcap_pve_alt', 'Subcap PvE Alt'), ('subcap_pvp_alt', 'Subcap PvP Alt'), ('industry_alt', 'Industry Alt'), ('useless_alt', 'Useless Alt')], max_length=255, null=True),
        ),
    ]