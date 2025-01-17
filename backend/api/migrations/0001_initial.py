# Generated by Django 5.1.4 on 2024-12-28 21:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mdh', models.CharField(max_length=50, unique=True)),
                ('cote', models.CharField(blank=True, max_length=50, null=True)),
                ('inventaire', models.CharField(blank=True, max_length=50, null=True)),
                ('opn', models.CharField(blank=True, max_length=50, null=True)),
                ('titre', models.CharField(max_length=255)),
                ('lieu_ed', models.CharField(blank=True, max_length=255, null=True)),
                ('suif_notes', models.TextField(blank=True, null=True)),
                ('public_notes', models.TextField(blank=True, null=True)),
                ('isbn_a', models.CharField(blank=True, max_length=50, null=True)),
                ('isbn_c', models.CharField(blank=True, max_length=50, null=True)),
                ('form_doss', models.CharField(blank=True, max_length=255, null=True)),
                ('s265b', models.CharField(blank=True, max_length=50, null=True)),
                ('specialite', models.CharField(blank=True, max_length=255, null=True)),
                ('nb_page', models.PositiveIntegerField(blank=True, null=True)),
                ('date_edition', models.DateField(blank=True, null=True)),
                ('editeur', models.CharField(blank=True, max_length=255, null=True)),
                ('prix', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('auteurs', models.ManyToManyField(related_name='articles', to='api.author')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mdh', models.CharField(max_length=50, unique=True)),
                ('cote', models.CharField(blank=True, max_length=50, null=True)),
                ('inventaire', models.CharField(blank=True, max_length=50, null=True)),
                ('opn', models.CharField(blank=True, max_length=50, null=True)),
                ('titre', models.CharField(max_length=255)),
                ('lieu_ed', models.CharField(blank=True, max_length=255, null=True)),
                ('suif_notes', models.TextField(blank=True, null=True)),
                ('public_notes', models.TextField(blank=True, null=True)),
                ('isbn_a', models.CharField(blank=True, max_length=50, null=True)),
                ('isbn_c', models.CharField(blank=True, max_length=50, null=True)),
                ('form_doss', models.CharField(blank=True, max_length=255, null=True)),
                ('s265b', models.CharField(blank=True, max_length=50, null=True)),
                ('specialite', models.CharField(blank=True, max_length=255, null=True)),
                ('nb_page', models.PositiveIntegerField(blank=True, null=True)),
                ('date_edition', models.DateField(blank=True, null=True)),
                ('editeur', models.CharField(blank=True, max_length=255, null=True)),
                ('prix', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('auteurs', models.ManyToManyField(related_name='books', to='api.author')),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrows', to='api.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrows', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mdh', models.CharField(max_length=50, unique=True)),
                ('cote', models.CharField(blank=True, max_length=50, null=True)),
                ('inventaire', models.CharField(blank=True, max_length=50, null=True)),
                ('opn', models.CharField(blank=True, max_length=50, null=True)),
                ('titre', models.CharField(max_length=255)),
                ('lieu_ed', models.CharField(blank=True, max_length=255, null=True)),
                ('suif_notes', models.TextField(blank=True, null=True)),
                ('public_notes', models.TextField(blank=True, null=True)),
                ('isbn_a', models.CharField(blank=True, max_length=50, null=True)),
                ('isbn_c', models.CharField(blank=True, max_length=50, null=True)),
                ('form_doss', models.CharField(blank=True, max_length=255, null=True)),
                ('s265b', models.CharField(blank=True, max_length=50, null=True)),
                ('specialite', models.CharField(blank=True, max_length=255, null=True)),
                ('nb_page', models.PositiveIntegerField(blank=True, null=True)),
                ('date_edition', models.DateField(blank=True, null=True)),
                ('editeur', models.CharField(blank=True, max_length=255, null=True)),
                ('prix', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('auteurs', models.ManyToManyField(related_name='research_papers', to='api.author')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.article')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.book')),
                ('research_paper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.researchpaper')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
