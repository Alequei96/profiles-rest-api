from rest_framework import serializers

class APISerializer(serializers.Serializer):
    """Serializers a name and lastname field for testing our APIView"""
    name = serializers.CharField(max_length = 10)
    lastname = serializers.CharField(max_length = 20)