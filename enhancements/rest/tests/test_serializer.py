from django.test import TestCase
from enhancements.rest.serializers import ModelSerializer
from enhancements.rest.registry import registry
from .models import Base, Child

from rest_framework.test import APIRequestFactory


class ChildSerializer(ModelSerializer):

    class Meta:
        model = Child

registry.register(Child, ChildSerializer)


class SerializerTestCase(TestCase):

    def setUp(self):
        self.child = Child.objects.create(id=2)
        self.base = Base.objects.create(name='1', child=self.child, id=1)

    def test_dynamic(self):
        class BaseSerializer(ModelSerializer):

            class Meta:
                model = Base
                pk_relations = ['child']

        s = BaseSerializer(self.base, exclude=['name', 'child'])
        self.assertEqual(s.data, {'id': 1})
        s = BaseSerializer(self.base, fields=['id'])
        self.assertEqual(s.data, {'id': 1})

    def test_pk_rel(self):
        class BaseSerializer(ModelSerializer):

            class Meta:
                model = Base
                pk_relations = ['child']

        s = BaseSerializer(self.base)
        self.assertEqual(s.data, {'id': 1, 'name': '1', 'child': 2})

    def test_nested(self):

        class BaseSerializer(ModelSerializer):

            class Meta:
                model = Base

        s = BaseSerializer(self.base)
        self.assertEqual(s.data, {'id': 1, 'name': '1', 'child': {'id': 2}})

    def test_url_rel(self):

        class BaseSerializer(ModelSerializer):

            class Meta:
                model = Base
                url_relations = 'child'

        factory = APIRequestFactory()
        request = factory.get('/')

        s = BaseSerializer(self.base, context={'request': request})
        self.assertEqual(s.data, {'id': 1, 'name': '1', 'child': '/2'})
