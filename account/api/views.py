from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.api.serializers import ResgistrationSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def api_registerAccount_view(request):

    if request.method == 'POST':
        serializer = ResgistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered a new user"
            data['email'] = account.email
            data['username'] = account.username
            data['token'] = Token.objects.get(user=account).key
        else:
            data = serializer.errors
        return Response(data=data)
