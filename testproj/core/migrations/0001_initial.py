# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table('core_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=64)),
            ('jabber', self.gf('django.db.models.fields.EmailField')(max_length=64)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('other', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('core', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table('core_contact')


    models = {
        'core.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '64'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'other': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['core']