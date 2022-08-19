from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

#Created at profiles_api file serializers
from profiles_api import serializers



class ApiView(APIView):
    """Test API View"""
    serializer_class = serializers.APISerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hallo', 'api_view': an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            lastname = serializer.validated_data.get('lastname')
            message = f'Hello {name} {lastname}'
            return Response ({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put (self,request, pk=None):
        """Handle updating an object"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Goodbye {name}'

            return Response ({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self,request, pk=None):
        """Handle a partial update of an object"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            lastname = serializer.validated_data.get('lastname')
            message = f'Wait {lastname}'
            return Response ({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class ViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.APISerializer

    def list(self,request):
        """Return a hello message"""

        a_viewset = [
            'Uses model operations for functions (list, create, retrieve, update, partial-update, destroy)',
            'Simple CRUD interface for the DB',
            'Quick and simple API',
            'Working with standard data structures',
        ]

        return Response ({'message': 'Hello', 'a_viewset': a_viewset})

    
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data= request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HHTP_400_BADD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request,pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request,pk=None):
        """Handle removing sn object"""
        return Response({'http_method': 'DELETE'})


