# myapp/serializers.py

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import BookModel

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'

    def validate(self, data):
        title = data.get('title')
        author = data.get('author')

        if not title.isalpha():
            raise ValidationError(
                {"status": 400,
                 "detail": "Title must contain only alphabetic characters."}
            )
        if BookModel.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {"status": 400,
                 "detail": "A book with this title and author already exists."}
            )
        return data
