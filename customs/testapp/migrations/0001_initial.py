# Generated by Django 2.1.15 on 2020-04-25 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Data2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customs_id', models.CharField(blank=True, max_length=50, null=True)),
                ('product_number', models.CharField(blank=True, max_length=50, null=True)),
                ('product_id', models.CharField(blank=True, max_length=50, null=True)),
                ('elements', models.CharField(blank=True, max_length=255, null=True)),
                ('text_elements', models.TextField(blank=True, null=True)),
                ('insert_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'data2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DirectoryFactorRel',
            fields=[
                ('uid', models.BigAutoField(primary_key=True, serialize=False)),
                ('enable', models.BooleanField(blank=True, null=True)),
                ('enable_test', models.BooleanField(blank=True, null=True)),
                ('enable_key', models.BooleanField(blank=True, null=True)),
                ('enabletime', models.DateTimeField(blank=True, null=True)),
                ('endtime', models.DateTimeField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=50, null=True)),
                ('crisis', models.FloatField(blank=True, null=True)),
                ('wrongwords', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'directory_factor_rel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sysdiagrams',
            fields=[
                ('name', models.CharField(max_length=128)),
                ('principal_id', models.IntegerField()),
                ('diagram_id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('definition', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sysdiagrams',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TCodingRules',
            fields=[
                ('element_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('element_name', models.CharField(blank=True, max_length=50, null=True)),
                ('enable_small_alp', models.IntegerField()),
                ('enable_big_alp', models.IntegerField(blank=True, null=True)),
                ('enable_figure', models.IntegerField()),
                ('length', models.IntegerField()),
            ],
            options={
                'db_table': 't_coding_rules',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TDirectoryCode',
            fields=[
                ('product_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, max_length=255, null=True)),
                ('enable_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('whether_enable', models.BooleanField(blank=True, db_column='Whether_enable', null=True)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 't_directory_code',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TFactorCode',
            fields=[
                ('element_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('element_name', models.CharField(max_length=255)),
                ('syno_code', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 't_factor_code',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WmdThresholdValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element_code', models.CharField(max_length=50)),
                ('value', models.FloatField()),
            ],
            options={
                'db_table': 'wmd_threshold_value',
                'managed': False,
            },
        ),
    ]
