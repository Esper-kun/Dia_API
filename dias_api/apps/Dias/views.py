from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

from dias_api.apps.Dias.models import Dia
from dias_api.apps.Dias.serializers import DiaSerializer


class ListaDiaView(APIView):
    def get(self, request, format=None):
        dia = Dia.objects.all()
        serializer = DiaSerializer(dia, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = DiaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors)


class DetalhesDiaView(APIView):
    def get(self, request, id_dia, format=None):
        try:
            instance = Dia.objects.get(id_dia=id_dia)
            serializer = DiaSerializer(instance)
            return Response(serializer.data)
        except Dia.DoesNotExist:
            pass
        
        return Response()

    def put(self, request, id_dia, format=None):
        try:
            instance = Dia.objects.get(id_dia=id_dia)
            serializer = DiaSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Dia.DoesNotExist:
            pass
        
        return Response()

    def delete(self, request, id_dia, format=None):
        try:
            instance = Dia.objects.get(id_dia=id_dia)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
        except Dia.DoesNotExist:
            return Response()
