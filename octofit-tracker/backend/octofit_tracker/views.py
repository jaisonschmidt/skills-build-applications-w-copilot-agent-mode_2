from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request):
    return Response({
        'users': '/users/',
        'teams': '/teams/',
        'activities': '/activities/',
        'leaderboard': '/leaderboard/',
        'workouts': '/workouts/',
    })
