from django.core.management.base import BaseCommand, CommandError
from text_unidecode import unidecode
import csv
import os

# change "artworks" to your app name and models to your model names 
from artworks.models import Artwork, Artist

class Command(BaseCommand):
    help = 'Loads data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('data_folder', type=str)

    def handle(self, *args, **options):
        artist_file = os.path.join(options['data_folder'], 'artist_data.csv')
        artwork_file = os.path.join(options['data_folder'], 'artwork_data.csv')

        # load artists
        with open(artist_file) as artist_in: 
            rdr = csv.reader(artist_in)
            next(rdr)  # skip header line
            for id,name,gender,dates,yearOfBirth,yearOfDeath,placeOfBirth,placeOfDeath,url in rdr:
                yearOfBirth = yearOfBirth if yearOfBirth else None
                yearOfDeath = yearOfDeath if yearOfDeath else None
                artist = Artist(
                    tate_id=id, 
                    name=name,
                    search_name=unidecode(name),
                    gender=gender,
                    place_of_birth=placeOfBirth, 
                    place_of_death=placeOfDeath,
                    birth_year=yearOfBirth,
                    death_year=yearOfDeath,
                    tate_url=url
                )
                artist.save()

        # load artworks
        with open(artwork_file) as artwork_in:
            rdr = csv.reader(artwork_in)
            next(rdr)  # skip header line
            for (id,accession_number,artist,artistRole,artistId,title,dateText,medium,creditLine,
                 year,acquisitionYear,dimensions,width,height,depth,units,inscription,thumbnailCopyright,
                 thumbnailUrl,url) in rdr:

                artist = Artist.objects.filter(tate_id=artistId).first()

                artwork = Artwork(
                    title=title,
                    search_title=unidecode(title),
                    date_text=dateText,
                    medium=medium,
                    credit_line=creditLine,
                    width=width,
                    height=height,
                    depth=depth,
                    units=units,
                    inscription=inscription,
                    acquisition_year=acquisitionYear,
                    thumbnail_url=thumbnailUrl,
                    tate_url=url,
                    artist=artist,
                )
                artwork.save()

        self.stdout.write(self.style.SUCCESS('Successfully loaded data'))
