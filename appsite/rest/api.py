from rest_framework import viewsets
from appsite.models import Users, Consultants, Category,Field
from .  import serializeapi 

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('username')
    serializer_class = serializeapi.UsersSerializer

class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all().order_by('name')
    serializer_class = serializeapi.FieldSerializer