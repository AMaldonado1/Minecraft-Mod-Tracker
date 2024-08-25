from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class ModInfoView(APIView):
    def get(self, request):
        return Response({"mod_name": "Hello"}, status=status.HTTP_200_OK)