# Generated by Django 3.0.3 on 2020-02-21 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phone_field.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_remove_product_active_on'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, max_length=240, null=True, verbose_name='Slug')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31, null=True, verbose_name='phone')),
                ('country', models.CharField(blank=True, max_length=240, null=True, verbose_name='Country')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('name', 'slug'),
            },
        ),
        migrations.CreateModel(
            name='OrgGroups',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('addedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='organization.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrgProducts',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('licenses', models.IntegerField(blank=True, default=10, null=True, verbose_name='Licenses')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start Date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End Date')),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='organization.Organization')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='product.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrgUsers',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('uniqueno', models.CharField(blank=True, max_length=120, null=True, verbose_name='Unique Number')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start Date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End Date')),
                ('addedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='organization.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrgProductUsers',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start Date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End Date')),
                ('addedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='organization.Organization')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='organization.OrgProducts')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='organization.OrgUsers')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrgGroupUsers',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start Date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End Date')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='organization.OrgGroups')),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='organization.Organization')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='organization.OrgUsers')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
