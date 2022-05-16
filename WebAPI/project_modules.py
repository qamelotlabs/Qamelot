from time import sleep
from celery import shared_task
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests

import schedule
import time
from os import system

from WebAPI.models import *