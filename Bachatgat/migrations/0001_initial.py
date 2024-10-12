# Generated by Django 3.2.12 on 2024-10-11 16:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyBaseModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BachatGatRegistration',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Bachatgat.mybasemodel')),
                ('bachatgat_name', models.CharField(max_length=255)),
                ('start_month', models.CharField(max_length=50)),
                ('start_year', models.CharField(max_length=4)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('member_count', models.IntegerField()),
                ('pid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('register_by', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
            bases=('Bachatgat.mybasemodel',),
        ),
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Bachatgat.mybasemodel')),
                ('account_number', models.CharField(max_length=20)),
                ('ifsc_code', models.CharField(max_length=11)),
                ('bank_name', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=100)),
            ],
            bases=('Bachatgat.mybasemodel',),
        ),
        migrations.CreateModel(
            name='MemberRegistration',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Bachatgat.mybasemodel')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=20)),
                ('entry_month', models.CharField(max_length=20)),
                ('entry_year', models.IntegerField()),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=100)),
                ('bachatgat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bachatgat.bachatgatregistration')),
            ],
            bases=('Bachatgat.mybasemodel',),
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Bachatgat.mybasemodel')),
                ('user_type', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('government_pro', models.CharField(max_length=255)),
                ('bank_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bachatgat.bankdetails')),
            ],
            bases=('Bachatgat.mybasemodel',),
        ),
        migrations.CreateModel(
            name='Savings',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Bachatgat.mybasemodel')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('date_of_contribution', models.DateField(auto_now_add=True)),
                ('fine', models.DecimalField(decimal_places=2, max_digits=12)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bachatgat.memberregistration')),
            ],
            bases=('Bachatgat.mybasemodel',),
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Bachatgat.mybasemodel')),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('start_date', models.DateTimeField(auto_now=True)),
                ('repayment_schedule', models.CharField(max_length=255)),
                ('loan_status', models.CharField(max_length=50)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bachatgat.memberregistration')),
            ],
            bases=('Bachatgat.mybasemodel',),
        ),
        migrations.CreateModel(
            name='FundDistribution',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Bachatgat.mybasemodel')),
                ('emergency_fund', models.DecimalField(decimal_places=2, max_digits=12)),
                ('event_fund', models.DecimalField(decimal_places=2, max_digits=12)),
                ('inverstment', models.DecimalField(decimal_places=2, max_digits=12)),
                ('bachatgat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bachatgat.bachatgatregistration')),
            ],
            bases=('Bachatgat.mybasemodel',),
        ),
    ]