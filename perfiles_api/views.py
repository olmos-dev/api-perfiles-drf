from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from perfiles_api import serializers
from perfiles_api.models import UserProfile
from perfiles_api import permissions

class HelloApiView(APIView):
  serializer_class = serializers.HelloSerializer

  def get(self, request, format= None):
    
    caracteristicas = [
      'Usa los metodos HTTP como una funcion get, post, patch, put, delete',
      'Es similar al tradicional Django View',
      'Da mayor control sobre la logica de tu aplicaciion',
      'Is mapedo manualmente a las URLs'
    ]

    return Response({'message': 'Hello world', 'caracteristicas':caracteristicas})
  
  def post(self, request):
    serializer = self.serializer_class(data = request.data)

    if serializer.is_valid():
      nombre = serializer.validated_data.get('nombre')
      mensaje = f'Hola {nombre}'
      return Response({'mensaje':mensaje})
    
    else:
      return Response(
        serializer.errors, 
        status=status.HTTP_400_BAD_REQUEST
      )
    
  def put(self, request, pk=None):
    return Response({'metodo':'PUT'})
  
  def patch(self, request, pk=None):
    return Response({'metodo':'PATCH'})
  
  def delete(self, request, pk=None):
    return Response({'metodo':'DELETE'})
  

class HelloViewSet(viewsets.ViewSet):
  serializer_class = serializers.HelloSerializer

  def list(self, request):
    a_viewset = [
      'Usa las acciones (listar, crear, ver,actualizar algunos, actualizar todos',
      'Automaticamente mapea las urls usando routers',
      'Prove mas funcionalidades con menos codigo'
    ]

    return Response({'message':'Hola', ' viwset: ':a_viewset})
  
  def create(self, request):
    serializer = self.serializer_class(data = request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('nombre')
      message = f'Hello {name}"!'
      return Response({'message':message})
    else:
      return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
      )
    
  def retrieve(self, request, pk=None):
    return Response({'metodo http: ', 'GET'})
  
  def update(self, request, pk=None):
    return Response({'metodo http: ', 'PUT'})
  
  def partial_update(self, request, pk=None):
    return Response({'metodo http: ', 'PATCH'})
  
  def destroy(self, request, pk=None):
    return Response({'metodo http: ', 'DELETE'})
  
class UserProfileViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.UserProfileSerializer
  queryset = UserProfile.objects.all()
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.UpdateOwnProfile,)
  filter_backends = (filters.SearchFilter,)
  search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
  renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


