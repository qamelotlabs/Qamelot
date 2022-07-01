from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from WebAPI.APIView.APICollection import *
from WebAPI.APIView.APICollectionStats import *
from TwitterApp.scraping_and_seeding.twitter_scraping import *
from NFTCollectionApp.Seeding.CollectionsSeeding import *
from dataScience.views import *
from .scheduler import *
from rest_framework.documentation import include_docs_urls
from django.conf.urls import url


urlpatterns = [
    # path('graphql', GraphQLView.as_view(graphiql=True)),

    url(r'^', include_docs_urls(title='Qamelot API Documentations')),
    path('admin/', admin.site.urls),
    path('',include('WebAPI.urls')),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]