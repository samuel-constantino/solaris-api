from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Character
from .serializers import CharacterSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def get_queryset(self):
        queryset = Character.objects.all()
        return queryset

    @action(detail=False, methods=['get'])
    def search_by_name(self, request):
        name = request.query_params.get('name', None)
        if name is not None:
            characters = Character.objects.filter(name__icontains=name)
            serializer = CharacterSerializer(characters, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Name parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.status_code = status.HTTP_200_OK
        return response

    @action(detail=False, methods=['put'])
    def edit_by_name(self, request):
        name = request.query_params.get('name', None)
        if name is not None:
            try:
                character = Character.objects.get(name=name)
                serializer = CharacterSerializer(character, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Character.DoesNotExist:
                return Response({"error": "Character not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Name parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.status_code = status.HTTP_201_CREATED
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.status_code = status.HTTP_200_OK
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
