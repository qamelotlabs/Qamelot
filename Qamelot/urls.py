from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from WebAPI.APIView.APICollection import *
from WebAPI.APIView.APICollectionStats import *
from TwitterApp.scraping_and_seeding.twitter_scraping import *
from NFTCollectionApp.Seeding.CollectionsSeeding import *
from dataScience.views import *
# from .scheduler import *

urlpatterns = [
    # path('graphql', GraphQLView.as_view(graphiql=True)),

    path('admin/', admin.site.urls),
    path('',include('WebAPI.urls')),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]