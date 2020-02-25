# Generated by Django 3.0.3 on 2020-02-25 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('ImageID', models.AutoField(primary_key=True, serialize=False)),
                ('ImageURL', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RightEyeVector',
            fields=[
                ('RightEyeVectorID', models.AutoField(primary_key=True, serialize=False)),
                ('Vector', models.TextField()),
                ('ImageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceProviderApp.Image')),
            ],
        ),
        migrations.CreateModel(
            name='RightEyebrowVector',
            fields=[
                ('RightEyebrowVectorID', models.AutoField(primary_key=True, serialize=False)),
                ('Vector', models.TextField()),
                ('ImageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceProviderApp.Image')),
            ],
        ),
        migrations.CreateModel(
            name='RightEarVector',
            fields=[
                ('RightEarVectorID', models.AutoField(primary_key=True, serialize=False)),
                ('Vector', models.TextField()),
                ('ImageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceProviderApp.Image')),
            ],
        ),
        migrations.CreateModel(
            name='NoseVector',
            fields=[
                ('NoseVectorID', models.AutoField(primary_key=True, serialize=False)),
                ('Vector', models.TextField()),
                ('ImageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceProviderApp.Image')),
            ],
        ),
        migrations.CreateModel(
            name='MouthVector',
            fields=[
                ('MouthVectorID', models.AutoField(primary_key=True, serialize=False)),
                ('Vector', models.TextField()),
                ('ImageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceProviderApp.Image')),
            ],
        ),
        migrations.CreateModel(
            name='LeftEyeVector',
            fields=[
                ('LeftEyeVectorID', models.AutoField(primary_key=True, serialize=False)),
                ('Vector', models.TextField()),
                ('ImageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceProviderApp.Image')),
            ],
        ),
        migrations.CreateModel(
            name='LeftEyebrowVector',
            fields=[
                ('LeftEyebrowVectorID', models.AutoField(primary_key=True, serialize=False)),
                ('Vector', models.TextField()),
                ('ImageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceProviderApp.Image')),
            ],
        ),
        migrations.CreateModel(
            name='LeftEarVector',
            fields=[
                ('LeftEarVectorID', models.AutoField(primary_key=True, serialize=False)),
                ('Vector', models.TextField()),
                ('ImageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceProviderApp.Image')),
            ],
        ),
        migrations.CreateModel(
            name='ChairVector',
            fields=[
                ('ChairVectorID', models.AutoField(primary_key=True, serialize=False)),
                ('Vector', models.TextField()),
                ('ImageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceProviderApp.Image')),
            ],
        ),
    ]