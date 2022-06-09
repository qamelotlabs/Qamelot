from Qamelot.project_modules import *


@shared_task
def collectionSeeding():
    print('Collection Seeding Process Begin')
    url = "https://top-nft-collections-and-sales.p.rapidapi.com/collections/1d"
    headers = {
    	"X-RapidAPI-Host": "top-nft-collections-and-sales.p.rapidapi.com",
    	"X-RapidAPI-Key": "b28fa39a67msh1e1b9cad88f1c6dp1ac287jsn0d12216c3e78"
    }
    response = requests.request("GET", url, headers=headers)
    resData = response.json()

    create_list = []
    for dta in resData:
        urlSlug = dta['collection_url'].rsplit('/', 1)[-1]

        getCollectionDetail     = NFTCollection.objects.filter(
        collection_name__iexact = dta['collection_name'], 
        slug__iexact            = urlSlug
        ).exists()

        if not getCollectionDetail:
            print('insert process running')
            create_list.append(
                NFTCollection(
            collection_url      = dta['collection_url'],
            slug                = urlSlug,
            collection_name     = dta['collection_name'],
            trades              = dta['trades'],
            volume              = dta['volume'],
            floor               = dta['floor']
            )
            )
        else:
            print('update process running')
            nftData = NFTCollection.objects.filter(
                collection_name__iexact = dta['collection_name'], 
                slug__iexact            = urlSlug
            ).update(
                trades              = dta['trades'],
                volume              = dta['volume'],
                floor               = dta['floor']
            )

    NFTCollection.objects.bulk_create(create_list)

# ------------------------------------------------------------------------------- #
    # for dta in resData:
    #     print(dta['collection_url'].rsplit('/', 1)[-1])

    #     urlSlug = dta['collection_url'].rsplit('/', 1)[-1]

    #     getCollectionDetail = NFTCollection.objects.filter(
    #         collection_name__iexact=dta['collection_name'], 
    #         slug__iexact=urlSlug
    #         ).exists()

    #     if getCollectionDetail is False:

    #         nftData = NFTCollection.objects.create(
    #             collection_url      = dta['collection_url'],
    #             slug                = urlSlug,
    #             collection_name     = dta['collection_name'],
    #             trades              = dta['trades'],
    #             volume              = dta['volume'],
    #             floor               = dta['floor']
    #         )
    #     else:
    #         nftData = NFTCollection.objects.filter(
    #             collection_name__iexact = dta['collection_name'], 
    #             slug__iexact            = urlSlug
    #         ).update(
    #             trades              = dta['trades'],
    #             volume              = dta['volume'],
    #             floor               = dta['floor']
    #         )

# =================================================================================================== #

# By-week
# url = "https://top-nft-collections-and-sales.p.rapidapi.com/collections/7d"

# headers = {
# 	"X-RapidAPI-Host": "top-nft-collections-and-sales.p.rapidapi.com",
# 	"X-RapidAPI-Key": "b28fa39a67msh1e1b9cad88f1c6dp1ac287jsn0d12216c3e78"
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)

# By-month
# url = "https://top-nft-collections-and-sales.p.rapidapi.com/collections/30d"

# headers = {
# 	"X-RapidAPI-Host": "top-nft-collections-and-sales.p.rapidapi.com",
# 	"X-RapidAPI-Key": "b28fa39a67msh1e1b9cad88f1c6dp1ac287jsn0d12216c3e78"
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)
