from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
  def get(self, request, format= None):
    
    caracteristicas = [
      'Usa los metodos HTTP como una funcion get, post, patch, put, delete',
      'Es similar al tradicional Django View',
      'Da mayor control sobre la logica de tu aplicaciion',
      'Is mapedo manualmente a las URLs'
    ]
    
    return Response({'message': 'Hello world', 'caracteristicas':caracteristicas})