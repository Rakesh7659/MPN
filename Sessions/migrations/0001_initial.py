# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewSession'
        db.create_table(u'Sessions_newsession', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('event_type', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('_13_to_16_years', self.gf('django.db.models.fields.BooleanField')()),
            ('_17_to_21_years', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'Sessions', ['NewSession'])

        # Adding model 'GenerateReport'
        db.create_table(u'Sessions_generatereport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.IntegerField')()),
            ('attachment', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'Sessions', ['GenerateReport'])

        # Adding M2M table for field session on 'GenerateReport'
        m2m_table_name = db.shorten_name(u'Sessions_generatereport_session')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('generatereport', models.ForeignKey(orm[u'Sessions.generatereport'], null=False)),
            ('newsession', models.ForeignKey(orm[u'Sessions.newsession'], null=False))
        ))
        db.create_unique(m2m_table_name, ['generatereport_id', 'newsession_id'])


    def backwards(self, orm):
        # Deleting model 'NewSession'
        db.delete_table(u'Sessions_newsession')

        # Deleting model 'GenerateReport'
        db.delete_table(u'Sessions_generatereport')

        # Removing M2M table for field session on 'GenerateReport'
        db.delete_table(db.shorten_name(u'Sessions_generatereport_session'))


    models = {
        u'Sessions.generatereport': {
            'Meta': {'object_name': 'GenerateReport'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'session': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['Sessions.NewSession']", 'null': 'True', 'blank': 'True'})
        },
        u'Sessions.newsession': {
            'Meta': {'object_name': 'NewSession'},
            '_13_to_16_years': ('django.db.models.fields.BooleanField', [], {}),
            '_17_to_21_years': ('django.db.models.fields.BooleanField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'event_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['Sessions']