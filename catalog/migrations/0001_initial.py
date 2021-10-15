# Generated by Django 3.2.7 on 2021-10-15 19:36

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import modelcluster.contrib.taggit
import modelcluster.fields
import streams.blocks
import wagtail.contrib.routable_page.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaintingCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
            ],
            options={
                'verbose_name': 'Painting Category',
                'verbose_name_plural': 'Painting Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PaintingDetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('date', models.DateField(blank=True, null=True)),
                ('width', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('description', wagtail.core.fields.StreamField([('simple_richtext', streams.blocks.SimpleRichtextBlock())], blank=True, null=True)),
                ('links', wagtail.core.fields.StreamField([('links', wagtail.core.blocks.StructBlock([('button_title', wagtail.core.blocks.CharBlock(max_length=60, required=False)), ('button_text', streams.blocks.RichtextBlock(features=['bold', 'italic'], required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(help_text='If selected, this url will be used first', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If added, this url will be used secondarily to the button page', required=False))], blank=True, null=True))], blank=True, null=True)),
                ('initial_inventory', wagtail.core.fields.StreamField([('dbreference', wagtail.core.blocks.CharBlock(blank=True, default='a', help_text='Entry from initial Excel Inventory by JMC, for internal needs only', max_length=50, null=True)), ('remark', wagtail.core.blocks.CharBlock(blank=True, default='a', help_text='Entry from initial Excel Inventory by JMC, for internal needs only', max_length=150, null=True)), ('signature', wagtail.core.blocks.BooleanBlock(blank=True, detault='Yes', null=True))], blank=True, null=True)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('painter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PaintingIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subtitle', wagtail.core.fields.RichTextField(blank=True, help_text='Catchy, short informative description of the page', max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='PaintingLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
            ],
            options={
                'verbose_name': 'Painting Location',
                'verbose_name_plural': 'Painting Locations',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PaintingMedium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
            ],
            options={
                'verbose_name': 'Paining Medium',
                'verbose_name_plural': 'Painting Mediums',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PaintingSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
            ],
            options={
                'verbose_name': 'Paining Support',
                'verbose_name_plural': 'Painting Supports',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PaintingPageTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='catalog.paintingdetailpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalog_paintingpagetag_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='paintingdetailpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='catalog.PaintingPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='PaintingPagePaintingSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='supports', to='catalog.paintingdetailpage')),
                ('painting_support', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_pages', to='catalog.paintingsupport')),
            ],
            options={
                'unique_together': {('page', 'painting_support')},
            },
        ),
        migrations.CreateModel(
            name='PaintingPagePaintingMedium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='mediums', to='catalog.paintingdetailpage')),
                ('painting_medium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_pages', to='catalog.paintingmedium')),
            ],
            options={
                'unique_together': {('page', 'painting_medium')},
            },
        ),
        migrations.CreateModel(
            name='PaintingPagePaintingLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='catalog.paintingdetailpage')),
                ('painting_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_pages', to='catalog.paintinglocation')),
            ],
            options={
                'unique_together': {('page', 'painting_location')},
            },
        ),
        migrations.CreateModel(
            name='PaintingPagePaintingCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='catalog.paintingdetailpage')),
                ('painting_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_pages', to='catalog.paintingcategory')),
            ],
            options={
                'unique_together': {('page', 'painting_category')},
            },
        ),
    ]
