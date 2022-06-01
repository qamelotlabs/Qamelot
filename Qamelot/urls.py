from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from WebAPI.scraping_and_seeding.image_scraping import *
from WebAPI.scraping_and_seeding.twitter_scraping import *
from WebAPI.scraping_and_seeding.collection_scraping import *
<<<<<<< HEAD
=======
from WebAPI.scraping_and_seeding.rarible_scraping import *
>>>>>>> develop
# from .scheduler import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('WebAPI.urls')),
    # path('graphql', GraphQLView.as_view(graphiql=True)),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]