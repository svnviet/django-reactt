from rest_framework import serializers
from .models import Blog
from res_users.models import Customer


class FilmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id',
                  'title', 'storyline', 'genres', 'stars', 'creators', 'languages', 'release_date', 'runtime',
                  'trailer',
                  'poster', 'production_companies')
