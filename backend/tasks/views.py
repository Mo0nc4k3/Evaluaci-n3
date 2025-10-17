from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Tarea
from .serializers import TareaSerializer 

class TareaPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'page'

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all().order_by('-created_at')
    serializer_class = TareaSerializer
    pagination_class = TareaPagination
    http_method_names = ['get', 'post', 'patch', 'delete']
