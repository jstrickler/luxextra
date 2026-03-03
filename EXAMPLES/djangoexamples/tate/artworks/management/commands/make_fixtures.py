from pprint import pprint
from django.core.management.base import BaseCommand, CommandError
import os
import json
from artworks.models import Artwork, Artist
from uuid import UUID

class Command(BaseCommand):
    help = 'Dumps data from Tate DB into JSON files'

    def add_arguments(self, parser):
        parser.add_argument('fixture_path', type=str)
        parser.add_argument('max_records', type=int, default=10)

    @staticmethod
    def make_dict(obj, model_name):
        obj_dict = {'model': model_name}

        temp_dict = dict(obj.__dict__)
        temp_dict.pop('_state')

        obj_dict['pk'] = str(temp_dict.pop('id'))

        for field, value in temp_dict.items():
            if field.endswith('id'):
                temp_dict[field] = str(value)

        obj_dict['fields'] = temp_dict
        
        return obj_dict

    def handle(self, *args, **options):
        max_records = options['max_records']
        fixture_path = options['fixture_path']

        records = []

        for artist in Artist.objects.all()[:max_records]:
            records.append(self.make_dict(artist, 'artworks.artist'))

            for artwork in artist.artworks.all():
                records.append(self.make_dict(artwork, 'artworks.artwork'))

        with open(fixture_path, "w") as fixture_out:
            json.dump(records, fixture_out, indent=4)