from time import sleep
from celery import shared_task
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests
from django.conf import settings
import boto3
import schedule
import time
from datetime import datetime, timedelta
from os import system
from urllib.parse import urlparse
from django.db.models import Q
from multiprocessing import Process

from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from datetime import date, timedelta, datetime
import datetime

from WebAPI.models import *
from NFTCollectionApp.models import *
from TwitterApp.models import *


errorMsg = {
    'error'		: True,
    'message'	: 'Service temporarily unavailable, try again later'
}

s3 = boto3.resource(
    's3', 
    region_name=settings.AWS_S3_REGION, 
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )

def runParallel(*functions):
    '''
    Run functions in parallel
    '''
    from multiprocessing import Process
    processes = []
    for function in functions:
        proc = Process(target=function)
        proc.start()
        processes.append(proc)
    for proc in processes:
        proc.join()

