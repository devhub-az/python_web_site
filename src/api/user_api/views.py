from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer


@api_view(['POST',])
def register(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Ugurla qeydiyyyatdan kecdiniz'
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)




