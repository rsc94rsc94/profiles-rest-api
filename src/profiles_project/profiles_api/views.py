from django.shortcuts import render


from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from . import serializers
from . import models
from . import permissions

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as a function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you most control over your logic',
            'is mapped manually to URLS'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, reqest, pk=None):
        """Handles updating the oject."""

        return Response({'method': 'put'})


    def patch(self, reqest, pk=None):
        """Path reqest only updates fields provided in the request."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Delets an object."""

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSets"""

    serializer_class = serializers.HelloSerializer
    def list(self,reqest):
        """Returns a Hello Message"""

        a_viewset=[
            'Uses actions (list,create,retrive,update partia_update)',
            'Automatically maps to URLs using our Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self,reqest):
        """create a new hello message"""

        serializer = serializers.HelloSerializer(data=reqest.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message =  'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, reqest, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method':'GET'})

    def update(self, reqest, pk=None):
        """Handles updating an object"""

        return Response({'http method':'PUT'})

    def partial_update(self, reqest, pk=None):
        """Hanndles updating part of an object"""

        return Response({'http method': 'PATCH'})

    def destroy(self, reqest, pk=None):
        """Handles removing part of an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating reading and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.object.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
