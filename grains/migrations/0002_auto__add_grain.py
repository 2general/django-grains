# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Grain'
        db.create_table(u'grains_grain', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=1024, db_index=True)),
            ('content_type', self.gf('django.db.models.fields.CharField')(default='text/plain', max_length=255)),
            ('value', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'grains', ['Grain'])


    def backwards(self, orm):
        # Deleting model 'Grain'
        db.delete_table(u'grains_grain')


    models = {
        u'grains.grain': {
            'Meta': {'object_name': 'Grain'},
            'content_type': ('django.db.models.fields.CharField', [], {'default': "'text/plain'", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1024', 'db_index': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['grains']