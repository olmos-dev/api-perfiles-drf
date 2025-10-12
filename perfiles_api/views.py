from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from perfiles_api import serializers


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