from .serializers import RegisterSerializers
from rest.frame_work.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView

class UserRegistration(APIView):
    def post(self,request);
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response('Account is created', status = 201)