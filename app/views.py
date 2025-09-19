from rest_framework import viewsets, generics
from .models import BookModel
from .serializers import BookSerializer
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    
class BookDetailView(generics.RetrieveAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer