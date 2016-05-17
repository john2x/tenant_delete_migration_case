# -*- coding: utf-8 -*-
from customers.models import Client
from shared_app.models import SharedModel, ToBeDeletedModel, RelatedModel
from django.core.management.base import BaseCommand
from tenant_schemas.utils import schema_context


class Command(BaseCommand):
    help = 'Bootstrap test data'

    def handle(self, *args, **options):
        Client.objects.create(domain_url='localhost',
                              schema_name='public')

        Client.objects.create(domain_url='test.localhost',
                              schema_name='test')

        with schema_context('test'):
            rm01 = RelatedModel.objects.create(name='rm_01')
            rm02 = RelatedModel.objects.create(name='rm_02')

            sm01 = SharedModel.objects.create(name='sm_01', related_obj=rm01)

            tbdm01 = ToBeDeletedModel.objects.create(name='tbdm_01', related_obj=rm02)

            sm01.tags.add('foo')
            tbdm01.tags.add('bar')
