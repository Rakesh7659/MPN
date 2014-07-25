# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hobby'
        db.create_table(u'ymht_hobby', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'ymht', ['Hobby'])

        # Adding model 'Country'
        db.create_table(u'ymht_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'ymht', ['Country'])

        # Adding model 'State'
        db.create_table(u'ymht_state', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.Country'])),
        ))
        db.send_create_signal(u'ymht', ['State'])

        # Adding model 'City'
        db.create_table(u'ymht_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.State'])),
        ))
        db.send_create_signal(u'ymht', ['City'])

        # Adding model 'Event'
        db.create_table(u'ymht_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('held_on', self.gf('django.db.models.fields.DateField')()),
            ('category', self.gf('django.db.models.fields.IntegerField')()),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.City'])),
        ))
        db.send_create_signal(u'ymht', ['Event'])

        # Adding model 'YMHT'
        db.create_table(u'ymht_ymht', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='male', max_length=25)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('hobby', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.Hobby'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.Event'])),
            ('gnan_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('father_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('father_contact', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('mother_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('mother_contact', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('profile_picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'ymht', ['YMHT'])

        # Adding model 'YMHTMobile'
        db.create_table(u'ymht_ymhtmobile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ymht', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.YMHT'])),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ymht', ['YMHTMobile'])

        # Adding model 'YMHTEmail'
        db.create_table(u'ymht_ymhtemail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ymht', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.YMHT'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ymht', ['YMHTEmail'])

        # Adding model 'YMHTAddress'
        db.create_table(u'ymht_ymhtaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ymht', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.YMHT'])),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('address_3', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('landmark', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.City'])),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ymht', ['YMHTAddress'])

        # Adding model 'YMHTEducation'
        db.create_table(u'ymht_ymhteducation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ymht', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.YMHT'])),
            ('college', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('other_details', self.gf('django.db.models.fields.TextField')()),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'ymht', ['YMHTEducation'])

        # Adding model 'YMHTJob'
        db.create_table(u'ymht_ymhtjob', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ymht', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.YMHT'])),
            ('jobtype', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('experience', self.gf('django.db.models.fields.IntegerField')()),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('job_category', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('current', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'ymht', ['YMHTJob'])

        # Adding model 'Coordinator'
        db.create_table(u'ymht_coordinator', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('gnan_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'ymht', ['Coordinator'])

        # Adding model 'Center'
        db.create_table(u'ymht_center', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.IntegerField')()),
            ('established_since', self.gf('django.db.models.fields.DateField')()),
            ('locality', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('address_3', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('landmark', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.City'])),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal(u'ymht', ['Center'])

        # Adding M2M table for field coordinators on 'Center'
        m2m_table_name = db.shorten_name(u'ymht_center_coordinators')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('center', models.ForeignKey(orm[u'ymht.center'], null=False)),
            ('coordinator', models.ForeignKey(orm[u'ymht.coordinator'], null=False))
        ))
        db.create_unique(m2m_table_name, ['center_id', 'coordinator_id'])

        # Adding model 'Membership'
        db.create_table(u'ymht_membership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ymht', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.YMHT'])),
            ('coordinator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.Coordinator'])),
            ('center', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.Center'])),
            ('age_group', self.gf('django.db.models.fields.IntegerField')()),
            ('role', self.gf('django.db.models.fields.IntegerField')()),
            ('since', self.gf('django.db.models.fields.DateField')()),
            ('till', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'ymht', ['Membership'])

        # Adding model 'SevaDetails'
        db.create_table(u'ymht_sevadetails', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.Event'])),
            ('ymht', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.YMHT'])),
            ('coordinator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ymht.Coordinator'])),
            ('attended', self.gf('django.db.models.fields.IntegerField')()),
            ('attended_days', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'ymht', ['SevaDetails'])


    def backwards(self, orm):
        # Deleting model 'Hobby'
        db.delete_table(u'ymht_hobby')

        # Deleting model 'Country'
        db.delete_table(u'ymht_country')

        # Deleting model 'State'
        db.delete_table(u'ymht_state')

        # Deleting model 'City'
        db.delete_table(u'ymht_city')

        # Deleting model 'Event'
        db.delete_table(u'ymht_event')

        # Deleting model 'YMHT'
        db.delete_table(u'ymht_ymht')

        # Deleting model 'YMHTMobile'
        db.delete_table(u'ymht_ymhtmobile')

        # Deleting model 'YMHTEmail'
        db.delete_table(u'ymht_ymhtemail')

        # Deleting model 'YMHTAddress'
        db.delete_table(u'ymht_ymhtaddress')

        # Deleting model 'YMHTEducation'
        db.delete_table(u'ymht_ymhteducation')

        # Deleting model 'YMHTJob'
        db.delete_table(u'ymht_ymhtjob')

        # Deleting model 'Coordinator'
        db.delete_table(u'ymht_coordinator')

        # Deleting model 'Center'
        db.delete_table(u'ymht_center')

        # Removing M2M table for field coordinators on 'Center'
        db.delete_table(db.shorten_name(u'ymht_center_coordinators'))

        # Deleting model 'Membership'
        db.delete_table(u'ymht_membership')

        # Deleting model 'SevaDetails'
        db.delete_table(u'ymht_sevadetails')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ymht.center': {
            'Meta': {'object_name': 'Center'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address_3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.IntegerField', [], {}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.City']"}),
            'coordinators': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ymht.Coordinator']", 'symmetrical': 'False'}),
            'established_since': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landmark': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        u'ymht.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.State']"})
        },
        u'ymht.coordinator': {
            'Meta': {'object_name': 'Coordinator'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gnan_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'ymht.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ymht.event': {
            'Meta': {'object_name': 'Event'},
            'category': ('django.db.models.fields.IntegerField', [], {}),
            'held_on': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.City']"})
        },
        u'ymht.hobby': {
            'Meta': {'object_name': 'Hobby'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ymht.membership': {
            'Meta': {'object_name': 'Membership'},
            'age_group': ('django.db.models.fields.IntegerField', [], {}),
            'center': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.Center']"}),
            'coordinator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.Coordinator']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.IntegerField', [], {}),
            'since': ('django.db.models.fields.DateField', [], {}),
            'till': ('django.db.models.fields.DateField', [], {}),
            'ymht': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.YMHT']"})
        },
        u'ymht.sevadetails': {
            'Meta': {'object_name': 'SevaDetails'},
            'attended': ('django.db.models.fields.IntegerField', [], {}),
            'attended_days': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'coordinator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.Coordinator']"}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ymht': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.YMHT']"})
        },
        u'ymht.state': {
            'Meta': {'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ymht.ymht': {
            'Meta': {'object_name': 'YMHT'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.Event']"}),
            'father_contact': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'father_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'male'", 'max_length': '25'}),
            'gnan_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hobby': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.Hobby']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mother_contact': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'mother_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'profile_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'ymht.ymhtaddress': {
            'Meta': {'object_name': 'YMHTAddress'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address_3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'landmark': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ymht': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.YMHT']"}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        u'ymht.ymhteducation': {
            'Meta': {'object_name': 'YMHTEducation'},
            'college': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other_details': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ymht': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.YMHT']"})
        },
        u'ymht.ymhtemail': {
            'Meta': {'object_name': 'YMHTEmail'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ymht': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.YMHT']"})
        },
        u'ymht.ymhtjob': {
            'Meta': {'object_name': 'YMHTJob'},
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'current': ('django.db.models.fields.BooleanField', [], {}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'experience': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_category': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'jobtype': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ymht': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.YMHT']"})
        },
        u'ymht.ymhtmobile': {
            'Meta': {'object_name': 'YMHTMobile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ymht': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ymht.YMHT']"})
        }
    }

    complete_apps = ['ymht']