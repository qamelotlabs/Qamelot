import graphene

import WebAPI.APIView.schema
from graphene_django import DjangoObjectType, DjangoListField 
from NFTCollectionApp.models import *


class collectionType(DjangoObjectType): 
    class Meta:
        model = NFTCollection
        fields = "__all__"

class Query(graphene.ObjectType):
    all_collections = graphene.List(collectionType)
    collection = graphene.Field(collectionType, updated_at=graphene.String())

    def resolve_all_collections(self, info, **kwargs):
        return NFTCollection.objects.all()

    def resolve_collection(self, info, updated_at):
        return NFTCollection.objects.filter(updated_at=str(updated_at))


schema = graphene.Schema(query=Query)