from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def apiOverview(request):
    return Response("API base point " ,  safe = False)
