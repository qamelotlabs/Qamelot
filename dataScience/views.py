from django.shortcuts import render
from NFTCollectionApp.models import *
from TwitterApp.models import *
import numpy
import matplotlib.pyplot as plt
# Create your views here.

def fetchNFTVolume():
    nfts = NFTCollection.objects.values_list('oneDayVolume','sevenDayVolume','thirtyDayVolume').all()
    a = numpy.zeros(100,)
    j = 0
    for i in nfts:
        try:
            a[j] = float(i[0])
        except:
            pass 
        j += 1
    plt.plot(a)
    plt.show()
    plt.clf()
    print(nfts)
        
        
# fetchNFTVolume()

def fetchTwitterDataVolume(id):
    nfts = TweetData.objects.filter(id__exact= id)
#     for i in nfts:
#         print('result: ', i[0])
#         break
        
# fetchNFTVolume()
# fetchTwitterDataVolume('1538839021014556672')