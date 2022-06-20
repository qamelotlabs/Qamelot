from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from WebAPI import views
from WebAPI.APIView.APICollection import *

from django.urls import path
from graphene_django.views import GraphQLView

urlpatterns = [
    path('v2/collections/', getTopCollections.as_view()),
    path('graphql', GraphQLView.as_view(graphiql=True)),
]

urlpatterns = format_suffix_patterns(urlpatterns)