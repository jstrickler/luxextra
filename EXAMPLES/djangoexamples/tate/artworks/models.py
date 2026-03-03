import uuid
from django.db import models
from django.contrib.auth.models import User

#  gender,dates,yearOfBirth,yearOfDeath,placeOfBirth,placeOfDeath,url in rdr:

class Artist(models.Model):
    tate_id = models.IntegerField(default=0)
    name = models.CharField(max_length=256, help_text="Artist's full name")
    search_name = models.CharField(max_length=256, help_text="Artist's full name normalized for searching",null=True)
    gender = models.CharField(max_length=1, null=True, help_text="Binary gender designation")
    place_of_birth = models.CharField(null=True, max_length=256, help_text="Location of artist's birth")
    place_of_death = models.CharField(null=True, max_length=256, help_text="Location of artist's death")
    birth_year = models.IntegerField(null=True, help_text="Year the artist was born")
    death_year = models.IntegerField(null=True, help_text="Year the artist died")
    tate_url = models.URLField(null=True, help_text="Link to this artist at www.tate.org.uk")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text="Unique ID of this artist")

    def __str__(self):
        return self.name

class Artwork(models.Model):
    title = models.CharField(max_length=512, default=None, help_text="Title of the artwork")
    search_title = models.CharField(max_length=512, default=None, help_text="Title normalized for searching", null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True,
                               related_name="artworks", help_text="Artist who created this artwork")
    medium = models.CharField(max_length=256, default=None, help_text="Medium of the artwork")
    credit_line = models.CharField(max_length=256, default=None, help_text="Credit line of the artwork")
    acquisition_year = models.CharField(max_length=32, default=None, help_text="Year artwork acquired by Tate")
    width = models.CharField(max_length=32, help_text="Widgth of the artwork")
    height = models.CharField(max_length=32, help_text="Height of the artwork")
    depth = models.CharField(max_length=32, help_text="Depth of the artwork")
    units = models.CharField(max_length=16, help_text="Units for dimensions")
    inscription = models.CharField(max_length=512, default=None, help_text="Inscription of the artwork")
    date_text = models.CharField(max_length=128, help_text="Date artwork was completed (if known)")
    thumbnail_url = models.URLField(help_text="Link to a thumbnail of this artwork at www.tate.org.uk")
    tate_url = models.URLField(help_text="Link to a full image of this artwork at www.tate.org.uk")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,help_text="Unique ID of this artwork")

    def __str__(self):
        return f"{self.title} by {self.artist}"

    class Meta:
        ordering = ['title', 'artist__name']