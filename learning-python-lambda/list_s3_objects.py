#!/home/linuxbrew/.linuxbrew/bin/python3
import boto3

# getting aws mgmt console programatically:
session=boto3.session.Session(profile_name="kfsoladmin")

# get s3 console
s3_re=session.resource(service_name='s3',region_name="us-east-1")  # ipv resource kan je ook client nemen )


bucket_name="kfsolutions-email"  # 999+ objects
# first creaet the bucket object:
# Bucket(name)
    # Creates a Bucket resource.:

    # bucket = s3.Bucket('name')

bucket_object=s3_re.Bucket(bucket_name)
print(bucket_object.objects.all()) # geeft bucket object: s3.Bucket.objectsCollection(s3.Bucket(name='kfsolutions-email'), s3.ObjectSummary)
# dus dara moeten we door heen met for loop:
'''
cnt=1
for each_obj in bucket_object.objects.all():
    print(cnt,each_obj)
    cnt+=1
    
# geeft 2077 keys:

# 2076 s3.ObjectSummary(bucket_name='kfsolutions-email', key='vvlhcmsqihfu6m6f7uv1n1iqpcl6p5qmpq31ca01')
# 2077 s3.ObjectSummary(bucket_name='kfsolutions-email', key='vvulj5q75qf8n7rc774pkinf2bpr3d8st4fovc81')

# enkel de filename: ( key ):
cnt=1
for each_obj in bucket_object.objects.all():
    print(cnt,each_obj.key)
    cnt+=1
# geeft:
# 2076 vvlhcmsqihfu6m6f7uv1n1iqpcl6p5qmpq31ca01
# 2077 vvulj5q75qf8n7rc774pkinf2bpr3d8st4fovc81
# dit was met de resource object.

# maar nu met de client object:
'''
s3_cli=session.client(service_name='s3',region_name="us-east-1")
# dit is de S3 console.

# maar we willen met een bucket werken in de s3 console:
'''
print(s3_cli.list_objects(Bucket=bucket_name))
'''

# geeft een dict:
#{'ResponseMetadata': {'RequestId': 'B5TK8RBSXJ4ZFMEP', 'HostId': 'inkCyadq02ykkblj7wiXhL3beR9PcGRVXZPEXfLHxITkSZHFkEaNAccfLWt0FaOWAoRBIIIhcOc=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'inkCyadq02ykkblj7wiXhL3beR9PcGRVXZPEXfLHxITkSZHFkEaNAccfLWt0FaOWAoRBIIIhcOc=', 'x-amz-request-id': 'B5TK8RBSXJ4ZFMEP', 'date': 'Tue, 05 Apr 2022 13:42:24 GMT', 'x-amz-bucket-region': 'eu-west-1', 'content-type': 'application/xml', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 1}, 'IsTruncated': True, 'Marker': '', 'Contents': [{'Key': '01l3j4r2t1663qvuhgn02c9lhdl26bsvmn6lqoo1', 'LastModified': datetime.datetime(2020, 11, 1, 11, 4, 55, tzinfo=tzutc()), 'ETag': '"b20db1f10deb604ab819cdb4c33513ae"', 'Size': 19766, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': '1robroos', 'ID': '25ac1b55c258e708708ca3a714c283428f922f0661d9033b9d7524fb34069d4d'}}, {'Key': '03nht8spdsubmt0rsujff7mitc54j15nmqnju081', 'LastModified': datetime.datetime(2022, 3, 1, 0, 53, 50, tzinfo=tzutc()), 'ETag': '"1a78ce6e7f32c595e143621a128b8e37"', 'Size': 156735, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': '1robroos', 'ID': '25ac1b55c258e708708ca3a714c283428f922f0661d9033b9d7524fb34069d4d'}}, {'Key': '04676r209afuj4mik2062ujriprjj8b75ekji1o1', 'LastModified': datetime.datetime(2020, 5, 15, 6, 37, 35, tzinfo=tzutc()), 'ETag': '"3b31fc5b092ae7ceb13bd8a8c19c1618"', 'Size': 248766, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': '1robroos', 'ID': '25ac1b55c258e708708ca3a714c283428f922f0661d9033b9d7524fb34069d4d'}}, {'Key': '04hu5tqu1q8eq3e19117absg8ujeamtcmnakauo1', 'LastModified': datetime.datetime(2022, 2, 25, 14, 14, 56, tzinfo=tzutc()), 'ETag': '"39e895b9f14f96903aded38745f0f24e"', 'Size': 52382, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': '1robroos', 'ID': '25ac1b55c258e708708ca3a714c283428f922f0661d9033b9d7524fb34069d4d'}}, {'Key': '07bdvcj4mm4al3m

# let op : er staat Contents :

#'Contents': [{'Key': '01l3j4r2t1663qvuhgn02c9lhdl26bsvmn6lqoo1', 'LastModified': datetime.datetime(2020, 11, 1, 11, 4, 55, tzinfo=tzutc()), 'ETag': '"b20db1f10deb604ab819cdb4c33513ae"', 'Size': 19766, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': '1robroos', 'ID': 

# dat zie je ook in de response syntax op https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_objects

'''
print(s3_cli.list_objects(Bucket=bucket_name).get('Contents'))
'''
# geeft een list:
#[{'Key': '01l3j4r2t1663qvuhgn02c9lhdl26bsvmn6lqoo1', 'LastModified': datetime.datetime(2020, 11, 1, 11, 4, 55, tzinfo=tzutc()), 'ETag': '"b20db1f10deb604ab819cdb4c33513ae"', 'Size': 19766, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': '1robroos', 'ID': '25ac1b55c258e708708ca3a714c283428f922f0661d9033b9d7524fb34069d4d'}}, {'Key': '03nht8spdsubmt0rsujff7mitc54j15nmqnju081', 'LastModified': datetime.datetime(2022, 3, 1, 0, 53, 50, tzinfo=tzutc()), 'ETag': '"1a78ce6e7f32c595e143621a128b8e37"', 'Size': 156735, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': '1robroos', 'ID': '25ac1b55c258e708708ca3

# maar we willen de Key:
# dus een for loop:
'''
cnt=1
for each_object in s3_cli.list_objects(Bucket=bucket_name).get('Contents'):
    print(cnt,each_object.get('Key'))
    cnt+=1
'''    
# DIT GEEFT MAAR 1000 OBJECTS:

# 999 fftps3mjfu2v9pc6dcup8tq3g1gi96t1din3s001
# 1000 ffuu1bbgfsh3h6kf27i2n5jcamqft5bajdrufm81

# DUS WE HEBBEN EEN PAGINATOR NODIG.
# er zullen denk ik 3 pages gecreerd worden.

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Paginator.ListObjects


    # class S3.Paginator.ListObjects
    # paginator = client.get_paginator('list_objects')
    # paginate(**kwargs)
    # Creates an iterator that will paginate through responses from S3.Client.list_objects().

    # See also: AWS API Documentation

    # Request Syntax

    # response_iterator = paginator.paginate(
    #     Bucket='string',
    #     Delimiter='string',
    #     EncodingType='url',
    #     Prefix='string',
    #     RequestPayer='requester',
    #     ExpectedBucketOwner='string',
    #     PaginationConfig={
    #         'MaxItems': 123,
    #         'PageSize': 123,
    #         'StartingToken': 'string'
    #     }
    # )
s3_cli=session.client(service_name='s3',region_name="us-east-1")
paginator = s3_cli.get_paginator('list_objects')
# met een paginator objetc moet je pagina's maken:
response_iterator = paginator.paginate(Bucket=bucket_name) # dit betekent: creer automatisch het aantal benodigde pages.
# je hoeft je geen zorgen te maken over het aantal pages.
'''
for each_page in response_iterator:
    print("DIt is een pagina")
# geeft:
# DIt is een pagina
# DIt is een pagina
# DIt is een pagina

#Dus in de paginator.paginate zitten 3 pages.
cnt=1
for each_page in response_iterator:
    print("DIt is een pagina")
    for each_object in each_page:
        print(cnt,each_object)
        cnt+=1
        
#geeft:
# DIt is een pagina
# DIt is een pagina
# DIt is een pagina
# DIt is een pagina
# 1 ResponseMetadata
# 2 IsTruncated
# 3 Marker
# 4 Contents
# 5 Name
# 6 Prefix
# 7 MaxKeys
# 8 EncodingType
'''
cnt=1
for each_page in response_iterator:
    print("DIt is een pagina")
    for each_object in each_page['Contents']:
        print(cnt,each_object['Key'])
        cnt+=1
# DIt is een pagina
# 1 01l3j4r2t1663qvuhgn02c9lhdl26bsvmn6lqoo1
# 2 03nht8spdsubmt0rsujff7mitc54j15nmqnju081
# 3 04676r209afuj4mik2062ujriprjj8b75ekji1o1
# 4 04hu5tqu1q8eq3e19117absg8ujeamtcmnakauo1
# [.................]
# 999 fftps3mjfu2v9pc6dcup8tq3g1gi96t1din3s001
# 1000 ffuu1bbgfsh3h6kf27i2n5jcamqft5bajdrufm81
# DIt is een pagina
# 1001 fg22hgbgkckl01vieaglp674batvnd7apal3k101
# 1002 fg7bp655f1448f827liss6a3n1chr4ao22n3s001
# 1003 fgvoch6i147d2vemmi7pokvd6rbpqgv77gib92g1
# [.................]
# 998 uejp6052m6i8auvdlg35bo9oaqrv7k37ahbsfu81
# 1999 uel894juulmmqjudmg64k1qu1flajva5e9nvvg81
# 2000 ueu495sra3b0gak2id43ob47ilq3up2dqr154r01
# DIt is een pagina
# 2001 ug9dfh3vpmttti6ijrb9ug3b8eheg37fruf0sc01
# 2002 ug9poclcsm7bmmhf8is0dskkitr3d7lug7om2no1
# [.................]
# 2075 vvbediinpf1l8mddqjchrn76aepf2armf1uurko1
# 2076 vvlhcmsqihfu6m6f7uv1n1iqpcl6p5qmpq31ca01
# 2077 vvulj5q75qf8n7rc774pkinf2bpr3d8st4fovc81


# dus drie pagina's.
# iedere pagina's wordt doorgelopen  ( for each_page in response_iterator: ) 
# en in iedere pagina worden alles objects getoond for each_object in each_page['Contents']:

# je hebt geen paginator voor buckets.

# Met queries gebruik je paginators. Niet bijv bij het creeren van een bucket.
# Bekijk het ook zo: als er een paginator bestaat voor een bepaalde operatie, gebruik die dan !
# bijv voor s3:
        # The available paginators are:

        # S3.Paginator.ListMultipartUploads
        # S3.Paginator.ListObjectVersions
        # S3.Paginator.ListObjects
        # S3.Paginator.ListObjectsV2
        # S3.Paginator.ListParts


# for resource objects heb je geen paginator nodig.

