from django.shortcuts import render
from django.contrib.auth.models import User
from mainapp.models import SavedData
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from mainapp.generate_keywords import get_keywords


# Create your views here.
@permission_classes([AllowAny])
@authentication_classes([])
class SignUp(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.create_user(username=username, password=password)

        if user:
            return Response('ok')
        return Response('fail')


class GenerateResults(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        abstract = request.data.get('abstract')
        results = get_keywords(abstract)

        new_record = SavedData(username=request.user, abstract=abstract, keywords=results)
        new_record.save()

        return Response({'data': results})


class GetHistory(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = SavedData.objects.filter(username=request.user)
        real_data = list(data.values())
        return Response({'status': 'ok', 'data': real_data})

