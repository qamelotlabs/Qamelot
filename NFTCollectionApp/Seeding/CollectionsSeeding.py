from Qamelot.project_modules import *
from .image_scraping import *

@shared_task
def collectionSeeding():
    print('Collection Seeding Process Begin...')
    url = "https://top-nft-collections-and-sales.p.rapidapi.com/collections/1d"
    headers = {
    	"X-RapidAPI-Host": "top-nft-collections-and-sales.p.rapidapi.com",
    	"X-RapidAPI-Key": "b28fa39a67msh1e1b9cad88f1c6dp1ac287jsn0d12216c3e78"
    }
    response = requests.request("GET", url, headers=headers)
    resData = response.json()

    today = date.today()

    create_list = []
    for dta in resData:
        urlSlug = dta['collection_url'].rsplit('/', 1)[-1]

        getCollectionDetail     = NFTCollection.objects.filter(
        collectionName__iexact = dta['collection_name'], 
        slug__iexact            = urlSlug
        ).exists()

        if not getCollectionDetail:
            print('insert process running')
            getCollection = NFTCollection.objects.create(
            collectionUrl      = dta['collection_url'],
            slug                = urlSlug,
            collectionName     = dta['collection_name'],
            createdAt          = today,
            updatedAt          = today
            )

            print('getCollection: ', getCollection.id)

            OpenseaRes = requests.get(
                'https://api.opensea.io/api/v1/collection/{}'.format(urlSlug), 
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
            )

            OpenseaData = OpenseaRes.json()

            try:
                NFTCollection.objects.filter(
                    id__exact  = getCollection.id
                ).update(
                    collectionAddress           = OpenseaData['collection']['primary_asset_contracts'][0]['address'],
                    collectionType              = OpenseaData['collection']['primary_asset_contracts'][0]['asset_contract_type'],
                    collectionDescription       = OpenseaData['collection']['description'],
                    oneDayVolume                = OpenseaData['collection']['stats']['one_day_volume'],
                    oneDayChange                = OpenseaData['collection']['stats']['one_day_change'],
                    oneDaySales                 = OpenseaData['collection']['stats']['one_day_sales'],
                    oneDayAveragePrice          = OpenseaData['collection']['stats']['one_day_average_price'],
                    sevenDayVolume              = OpenseaData['collection']['stats']['seven_day_volume'],
                    sevenDayChange              = OpenseaData['collection']['stats']['seven_day_change'],
                    sevenDaySales               = OpenseaData['collection']['stats']['seven_day_sales'],
                    sevenDayAveragePrice        = OpenseaData['collection']['stats']['seven_day_average_price'],
                    thirtyDayVolume             = OpenseaData['collection']['stats']['thirty_day_volume'],
                    thirtyDayChange             = OpenseaData['collection']['stats']['thirty_day_change'],
                    thirtyDaySales              = OpenseaData['collection']['stats']['thirty_day_sales'],
                    thirtyDayAveragePrice       = OpenseaData['collection']['stats']['thirty_day_average_price'],
                    totalVolume                 = OpenseaData['collection']['stats']['total_volume'],
                    totalSales                  = OpenseaData['collection']['stats']['total_sales'],
                    totalSupply                 = OpenseaData['collection']['stats']['total_supply'],
                    count                       = OpenseaData['collection']['stats']['count'],
                    numOwners                   = OpenseaData['collection']['stats']['num_owners'],
                    averagePrice                = OpenseaData['collection']['stats']['average_price'],
                    numReports                  = OpenseaData['collection']['stats']['num_reports'],
                    marketCap                   = OpenseaData['collection']['stats']['market_cap'],
                    floorPrice                  = OpenseaData['collection']['stats']['floor_price'],
                    collectionSymbol            = OpenseaData['collection']['primary_asset_contracts'][0]['symbol'],
                    owner                       = OpenseaData['collection']['primary_asset_contracts'][0]['owner'],
                    externalLink                = OpenseaData['collection']['external_url'],
                    safelistRequestStatus       = OpenseaData['collection']['safelist_request_status'],
                    twitterUsername             = OpenseaData['collection']['twitter_username'],
                    discordUrl                  = OpenseaData['collection']['discord_url'],
                    updatedAt                  = today
                )

                if OpenseaData['collection']['image_url']:
                    collectionAddress   = OpenseaData['collection']['primary_asset_contracts'][0]['address']
                    collectionSymbol    = OpenseaData['collection']['primary_asset_contracts'][0]['symbol']
                    externalImageUrl    = OpenseaData['collection']['image_url']
                    imageSubname        = collectionSymbol + '_' + collectionAddress
                    new_meta_url        = uploadFile(externalImageUrl, imageSubname)
                    NFTCollection.objects.filter(
                    id__exact  = getCollection.id
                    ).update(
                        externalImageUrl            = OpenseaData['collection']['image_url'],
                        awsBucketImageUrl           = new_meta_url
                    )
            except:
                print('Not present in Opensea')

        else:

            print('update process running')
            NFTCollection.objects.filter(
                collectionName__iexact  = dta['collection_name'], 
                slug__iexact            = urlSlug
            ).update(
                updatedAt              = today
            )

            OpenseaRes = requests.get(
                'https://api.opensea.io/api/v1/collection/{}'.format(urlSlug), 
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
            )

            OpenseaData = OpenseaRes.json()
            
            try:
                NFTCollection.objects.filter(
                    collectionName__iexact  = dta['collection_name'], 
                    slug__iexact            = urlSlug
                ).update(
                    collectionAddress           = OpenseaData['collection']['primary_asset_contracts'][0]['address'],
                    collectionType              = OpenseaData['collection']['primary_asset_contracts'][0]['asset_contract_type'],
                    collectionDescription       = OpenseaData['collection']['description'],
                    oneDayVolume                = OpenseaData['collection']['stats']['one_day_volume'],
                    oneDayChange                = OpenseaData['collection']['stats']['one_day_change'],
                    oneDaySales                 = OpenseaData['collection']['stats']['one_day_sales'],
                    oneDayAveragePrice          = OpenseaData['collection']['stats']['one_day_average_price'],
                    sevenDayVolume              = OpenseaData['collection']['stats']['seven_day_volume'],
                    sevenDayChange              = OpenseaData['collection']['stats']['seven_day_change'],
                    sevenDaySales               = OpenseaData['collection']['stats']['seven_day_sales'],
                    sevenDayAveragePrice        = OpenseaData['collection']['stats']['seven_day_average_price'],
                    thirtyDayVolume             = OpenseaData['collection']['stats']['thirty_day_volume'],
                    thirtyDayChange             = OpenseaData['collection']['stats']['thirty_day_change'],
                    thirtyDaySales              = OpenseaData['collection']['stats']['thirty_day_sales'],
                    thirtyDayAveragePrice       = OpenseaData['collection']['stats']['thirty_day_average_price'],
                    totalVolume                 = OpenseaData['collection']['stats']['total_volume'],
                    totalSales                  = OpenseaData['collection']['stats']['total_sales'],
                    totalSupply                 = OpenseaData['collection']['stats']['total_supply'],
                    count                       = OpenseaData['collection']['stats']['count'],
                    numOwners                   = OpenseaData['collection']['stats']['num_owners'],
                    averagePrice                = OpenseaData['collection']['stats']['average_price'],
                    numReports                  = OpenseaData['collection']['stats']['num_reports'],
                    marketCap                   = OpenseaData['collection']['stats']['market_cap'],
                    floorPrice                  = OpenseaData['collection']['stats']['floor_price'],
                    collectionSymbol            = OpenseaData['collection']['primary_asset_contracts'][0]['symbol'],
                    owner                       = OpenseaData['collection']['primary_asset_contracts'][0]['owner'],
                    externalLink                = OpenseaData['collection']['external_url'],
                    safelistRequestStatus       = OpenseaData['collection']['safelist_request_status'],
                    twitterUsername             = OpenseaData['collection']['twitter_username'],
                    discordUrl                  = OpenseaData['collection']['discord_url'],
                    updatedAt                  = today
                )

                if OpenseaData['collection']['image_url']:
                    collectionAddress   = OpenseaData['collection']['primary_asset_contracts'][0]['address']
                    collectionSymbol    = OpenseaData['collection']['primary_asset_contracts'][0]['symbol']
                    externalImageUrl    = OpenseaData['collection']['image_url']
                    imageSubname        = collectionSymbol + '_' + collectionAddress
                    new_meta_url        = uploadFile(externalImageUrl, imageSubname)
                    NFTCollection.objects.filter(
                    collectionName__iexact  = dta['collection_name'], 
                    slug__iexact            = urlSlug
                    ).update(
                        externalImageUrl            = OpenseaData['collection']['image_url'],
                        awsBucketImageUrl           = new_meta_url
                    )
            except:
                print('Not present in Opensea')



            # OpenseaRes = requests.get(
            #     'https://api.opensea.io/api/v1/collection/{}/stats'.format(urlSlug), 
            #     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
            # )

            # OpenseaData = OpenseaRes.json()

            # NFTCollection.objects.filter(
            #     collectionName__iexact  = dta['collection_name'], 
            #     slug__iexact            = urlSlug
            # ).update(
            #     oneDayVolume                = OpenseaData['stats']['one_day_volume'],
            #     oneDayChange                = OpenseaData['stats']['one_day_change'],
            #     oneDaySales                 = OpenseaData['stats']['one_day_sales'],
            #     oneDayAveragePrice          = OpenseaData['stats']['one_day_average_price'],
            #     sevenDayVolume              = OpenseaData['stats']['seven_day_volume'],
            #     sevenDayChange              = OpenseaData['stats']['seven_day_change'],
            #     sevenDaySales               = OpenseaData['stats']['seven_day_sales'],
            #     sevenDayAveragePrice        = OpenseaData['stats']['seven_day_average_price'],
            #     thirtyDayVolume             = OpenseaData['stats']['thirty_day_volume'],
            #     thirtyDayChange             = OpenseaData['stats']['thirty_day_change'],
            #     thirtyDaySales              = OpenseaData['stats']['thirty_day_sales'],
            #     thirtyDayAveragePrice       = OpenseaData['stats']['thirty_day_average_price'],
            #     totalVolume                 = OpenseaData['stats']['total_volume'],
            #     totalSales                  = OpenseaData['stats']['total_sales'],
            #     totalSupply                 = OpenseaData['stats']['total_supply'],
            #     count                       = OpenseaData['stats']['count'],
            #     numOwners                   = OpenseaData['stats']['num_owners'],
            #     averagePrice                = OpenseaData['stats']['average_price'],
            #     numReports                  = OpenseaData['stats']['num_reports'],
            #     marketCap                   = OpenseaData['stats']['market_cap'],
            #     floorPrice                  = OpenseaData['stats']['floor_price'],
            #     updated_at                  = today
            # )


# collectionSeeding()