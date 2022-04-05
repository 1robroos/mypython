import boto3

custom_session=boto3.session.Session(profile_name="kfsoladmin")
s3_re=custom_session.resource(service_name="s3",region_name="us-east-1")
print(s3_re.buckets.all())
    # geeft object terug: s3.bucketsCollection(s3.ServiceResource(), s3.Bucket)
    # Hier zit ale je bucket info in, dus je hebt een for loop nodig:
'''
for each_bucket_info in s3_re.buckets.all():
    print(each_bucket_info)
    # geeft al mn buckets met metadata er om heen:
    
    # s3.Bucket(name='969526043371-api-gateway-access')
    # s3.Bucket(name='athlondemo-bootstrap-terraform-state-dev')
    # s3.Bucket(name='athlondemo-bootstrap-terraform-state-stg')
    
    # dat is niet pretty,
    
# maak pretty:
for each_bucket_info in s3_re.buckets.all():
    print(each_bucket_info.name)
    # geeft:
    #969526043371-api-gateway-access
    #athlondemo-bootstrap-terraform-state-dev
    #athlondemo-bootstrap-terraform-state-stg
'''    
# nu met client object
print("________________________________________")
s3_cli=custom_session.client(service_name="s3",region_name="us-east-1")
'''
print(s3_cli.list_buckets())
# geeft altijd een dictionary:
#{u'Owner': {u'DisplayName': '1robroos', u'ID': '25ac1b55c258e708708ca3a714c283428f922f0661d9033b9d7524fb34069d4d'}, u'Buckets': [{u'CreationDate': datetime.datetime(2021, 4, 4, 20, 1, 31, tzinfo=tzutc()), u'Name': '969526043371-api-gateway-access'}, {u'CreationDate': datetime.datetime(2022, 2, 2, 12, 41, 47, tzinfo=tzutc()), u'Name': 'athlondemo-bootstrap-terraform-state-dev'}, {u'CreationDate': datetime.datetime(2022, 2, 2, 13, 57, 28, tzinfo=tzutc()), u'Name': 'athlondemo-bootstrap-terraform-state-stg'}, {u'CreationDate': datetime.datetime(2022, 2, 2, 12, 47, 51, tzinfo=tzutc()), u'Name': 'athlondemo-rstudio-terraform-state-dev'}, {u'CreationDa
'''
'''
print(s3_cli.list_buckets().get('Buckets'))
# nu krijg je een list:
#[{u'CreationDate': datetime.datetime(2021, 4, 4, 20, 1, 31, tzinfo=tzutc()), u'Name': '969526043371-api-gateway-access'}, {u'CreationDate': datetime.datetime(2022, 2, 2, 12, 41, 47, tzinfo=tzutc()), u'Name': 'athlondemo-bootstrap-terraform-state-dev'}, {u'CreationDate': datetime.datetime(2022, 2, 2, 13, 57, 28, tzinfo=tzutc()), u'Name': 'athlondemo-bootstrap-terraform-state-stg'}, {u'CreationDate': datetime.datetime(2022, 2, 2, 12, 47, 51, tzinfo=tzutc()), u'Name': 'athlondemo-rstudio-terraform-state-dev'}, {u'CreationDate': datetime.datetime(2022,
# met een for loop door de list heen:
for each_bucket_info in s3_cli.list_buckets().get('Buckets'):
    print(each_bucket_info)
# geeft een dict voor iedere bucket:
# {u'CreationDate': datetime.datetime(2021, 4, 4, 20, 1, 31, tzinfo=tzutc()), u'Name': '969526043371-api-gateway-access'}
# {u'CreationDate': datetime.datetime(2022, 2, 2, 12, 41, 47, tzinfo=tzutc()), u'Name': 'athlondemo-bootstrap-terraform-state-dev'}
# {u'CreationDate': datetime.datetime(2022, 2, 2, 13, 57, 28, tzinfo=tzutc()), u'Name': 'athlondemo-bootstrap-terraform-state-stg'}
# {u'CreationDate': datetime.datetime(2022, 2, 2, 12, 47, 51, tzinfo=tzutc()), u'Name': 'athlondemo-rstudio-terraform-state-dev'}

# maar we willen enkel de name zien:
for each_bucket_info in s3_cli.list_buckets().get('Buckets'):
    print(each_bucket_info.get('Name'))
# geeft:
# 969526043371-api-gateway-access
# athlondemo-bootstrap-terraform-state-dev
# athlondemo-bootstrap-terraform-state-stg

# maar met de client object: s3 laat enkel 1000 results zien !
# als best practice: gebruik altijd paginator!

'''
