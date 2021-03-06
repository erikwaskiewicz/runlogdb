# Generated by Django 2.0.6 on 2018-07-03 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_auto_20180629_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nextseq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument_id', models.CharField(max_length=100)),
                ('application_name', models.CharField(max_length=100)),
                ('application_version', models.CharField(max_length=100)),
                ('RTA_version', models.CharField(max_length=100)),
                ('systemsuite_version', models.CharField(max_length=100)),
                ('flowcell_serial', models.CharField(max_length=100)),
                ('PR2_serial_no', models.CharField(max_length=100)),
                ('reagent_serial_no', models.CharField(max_length=100)),
                ('experiment_name', models.CharField(max_length=100)),
                ('library_id', models.CharField(max_length=100)),
                ('chemistry', models.CharField(max_length=100)),
                ('focus_method', models.CharField(max_length=100)),
                ('surface_to_scan', models.CharField(max_length=100)),
                ('paired_end', models.CharField(max_length=100)),
                ('custom_R1_primer', models.CharField(max_length=100)),
                ('custom_R2_perimer', models.CharField(max_length=100)),
                ('custom_index_primer', models.CharField(max_length=100)),
                ('custom_index2_primer', models.CharField(max_length=100)),
                ('uses_custom_R1_primer', models.CharField(max_length=100)),
                ('uses_custom_R2_perimer', models.CharField(max_length=100)),
                ('uses_custom_index_primer', models.CharField(max_length=100)),
                ('uses_custom_index2_primer', models.CharField(max_length=100)),
                ('run_management_type', models.CharField(max_length=100)),
                ('basespace_id', models.CharField(max_length=100)),
                ('basespace_runmode', models.CharField(max_length=100)),
                ('computer_name', models.CharField(max_length=100)),
                ('max_reagent_kit_cycles', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='runlog',
            name='I5',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='runlog',
            name='I7',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='runlog',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='runlog',
            name='samples',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='runlog',
            name='pipeline',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='runlog',
            name='plates',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='nextseq',
            name='run_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Runlog'),
        ),
    ]
