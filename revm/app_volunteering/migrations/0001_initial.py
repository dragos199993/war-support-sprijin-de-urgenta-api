# Generated by Django 3.2.12 on 2022-03-01 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='type name')),
                ('description', models.CharField(blank=True, default='', max_length=500, verbose_name='type description')),
            ],
            options={
                'verbose_name': 'volunteering type',
                'verbose_name_plural': 'volunteering types',
            },
        ),
        migrations.CreateModel(
            name='VolunteeringRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=500, verbose_name='resource description')),
                ('county_coverage', models.CharField(choices=[('AB', 'Alba'), ('AR', 'Arad'), ('AG', 'Argeș'), ('BC', 'Bacău'), ('BH', 'Bihor'), ('BN', 'Bistrița-Năsăud'), ('BT', 'Botoșani'), ('BV', 'Brașov'), ('BR', 'Brăila'), ('B', 'București'), ('BZ', 'Buzău'), ('CL', 'Călărași'), ('CS', 'Caraș-Severin'), ('CJ', 'Cluj'), ('CT', 'Constanța'), ('CV', 'Covasna'), ('DB', 'Dâmbovița'), ('DJ', 'Dolj'), ('GL', 'Galați'), ('GR', 'Giurgiu'), ('GJ', 'Gorj'), ('HR', 'Harghita'), ('HD', 'Hunedoara'), ('IL', 'Ialomița'), ('IS', 'Iași'), ('IF', 'Ilfov'), ('MM', 'Maramureș'), ('MH', 'Mehedinți'), ('MS', 'Mureș'), ('NT', 'Neamț'), ('OT', 'Olt'), ('PH', 'Prahova'), ('SM', 'Satu Mare'), ('SJ', 'Sălaj'), ('SB', 'Sibiu'), ('SV', 'Suceava'), ('TR', 'Teleorman'), ('TM', 'Timiș'), ('TL', 'Tulcea'), ('VS', 'Vaslui'), ('VL', 'Vâlcea'), ('VN', 'Vrancea'), ('RO', 'Național')], max_length=2, verbose_name='county')),
                ('town', models.CharField(max_length=100, verbose_name='town')),
                ('added_on', models.DateTimeField(auto_now_add=True, verbose_name='resource added on')),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_volunteering.type')),
            ],
            options={
                'verbose_name': 'volunteering request',
                'verbose_name_plural': 'volunteering requests',
            },
        ),
        migrations.CreateModel(
            name='VolunteeringOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=500, verbose_name='resource description')),
                ('county_coverage', models.CharField(choices=[('AB', 'Alba'), ('AR', 'Arad'), ('AG', 'Argeș'), ('BC', 'Bacău'), ('BH', 'Bihor'), ('BN', 'Bistrița-Năsăud'), ('BT', 'Botoșani'), ('BV', 'Brașov'), ('BR', 'Brăila'), ('B', 'București'), ('BZ', 'Buzău'), ('CL', 'Călărași'), ('CS', 'Caraș-Severin'), ('CJ', 'Cluj'), ('CT', 'Constanța'), ('CV', 'Covasna'), ('DB', 'Dâmbovița'), ('DJ', 'Dolj'), ('GL', 'Galați'), ('GR', 'Giurgiu'), ('GJ', 'Gorj'), ('HR', 'Harghita'), ('HD', 'Hunedoara'), ('IL', 'Ialomița'), ('IS', 'Iași'), ('IF', 'Ilfov'), ('MM', 'Maramureș'), ('MH', 'Mehedinți'), ('MS', 'Mureș'), ('NT', 'Neamț'), ('OT', 'Olt'), ('PH', 'Prahova'), ('SM', 'Satu Mare'), ('SJ', 'Sălaj'), ('SB', 'Sibiu'), ('SV', 'Suceava'), ('TR', 'Teleorman'), ('TM', 'Timiș'), ('TL', 'Tulcea'), ('VS', 'Vaslui'), ('VL', 'Vâlcea'), ('VN', 'Vrancea'), ('RO', 'Național')], max_length=2, verbose_name='county')),
                ('town', models.CharField(max_length=100, verbose_name='town')),
                ('added_on', models.DateTimeField(auto_now_add=True, verbose_name='resource added on')),
                ('available_from', models.DateTimeField(auto_now_add=True, verbose_name='resource available from')),
                ('available_until', models.DateTimeField(null=True, verbose_name='resource available until')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_volunteering.type')),
            ],
            options={
                'verbose_name': 'volunteering offer',
                'verbose_name_plural': 'volunteering offers',
            },
        ),
        migrations.CreateModel(
            name='ResourceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_volunteering.volunteeringrequest')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_volunteering.volunteeringoffer')),
            ],
            options={
                'verbose_name': 'Offer - Request',
                'verbose_name_plural': 'Offer - Request',
            },
        ),
    ]
