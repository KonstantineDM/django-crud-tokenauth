from authapp.api.serializers import RegisterSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response


@api_view(['POST', ])
@authentication_classes([TokenAuthentication])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['status'] = 'Registration successful.'
        data['username'] = user.username
        data['email'] = user.email
        token = Token.objects.get(user=user).key
        data['Authorization'] = "Token " + token
    else:
        data = serializer.errors
    return Response(data)
