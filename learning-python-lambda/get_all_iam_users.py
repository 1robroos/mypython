import boto3

session=boto3.session.Session(profile_name="kfsoladmin") 
iam_re=session.resource("iam")
'''
cnt=1
for each_user in iam_re.users.all():
    print cnt,each_user.user_name
    cnt+=1
    
    
iam_cli=session.client("iam")
cnt=1
for each_user in iam_cli.list_users()['Users']:
    print cnt,each_user['UserName']
    cnt+=1
''' 
    
iam_cli=session.client("iam")
paginator = iam_cli.get_paginator('list_users')
#print(paginator.paginate()) # geeft een iterator: <botocore.paginate.PageIterator object at 0x7f2d54a7bfd0>
'''
cnt=1
for each_page in paginator.paginate():
    #print(each_page) # dit laat alle pagineas zien.{u'Users': [{u'UserName': '1robroos@gmail.com', u'PasswordLastUsed': datetime.datetime(2022, 3, 19, 20, 55, 34, tzinfo=tzutc()), u'CreateDate': datetime.datetime(2022, 3, 19, 20, 50, 8, tzinfo=tzutc()), u'UserId': 'AIDA6DPCBMLV7GA5YXXRJ', u'Path': '/', u'Arn': 'arn:a
    #print(each_page['Users']) # geeft list met users: [{u'UserName': '1robroos@gmail.com', u'PasswordLastUsed': datetime.datetime(2022, 3, 19, 20, 55, 34, tzinfo=tzutc()), u'CreateDate': datetime.datetime(2022, 3, 19, 20, 50, 8, tzinfo=tzutc()), u'UserId': 'AIDA6DPCBMLV7GA5YXXRJ', u'Path': '/', u'Arn': 'arn:aws:iam::969526043371:user/1robroos@gmail.com'}, {u'UserName': 'alice', u'PasswordLastUsed': datetime.datetime(2017, 9, 4, 7, 1, 43, tzinfo=tzutc()), u'CreateDate': datetime.datetime(2017, 9, 3, 18, 12, 36, tzinfo=tzutc()), u'UserId': 'AIDAJWPIUTOVOXFQYNWOC', u'Path': '/', u'Arn': 'arn:aws:ia
    #print(len(each_page['Users'])) # geeft bij mij 36 , bij author 100 100 4 ( 204 iam users )
    for each_user in  each_page['Users']:
        print(cnt,each_user['UserName']) # geeft alle usernamen op alle pagina's.
        cnt+=1
''' 
#################################################################################################################        
# Now for example for roles
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListRoles
'''
iam_cli=session.client("iam")
paginator = iam_cli.get_paginator('list_roles')
cnt=1
for each_page in paginator.paginate():
        for each_role in  each_page['Roles']:
            print(cnt,each_role['RoleName']) # geeft alle rolenamen op alle pagina's.
            cnt+=1
''' 
    # geeft alle rollen:
    #     laatste:
    #         (152, 'testwhatapigatewayiscreateid-role-1dsn74w5')
    # (153, 'timerhello-role-0t1ejjfu')
    # (154, 'VueFormulateUpload')
    # (155, 'workspaces_DefaultRole')
    # (156, 'xplusy-role-p0tz6tqn')
    # (157, 'YoutubeFunction-role-krbr9696')


#################################################################################################################        
# Now for example for objects in S3 bucket https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#paginators
'''
Request Syntax

response_iterator = paginator.paginate(
    Bucket='string',
    ..
    ..

Response Syntax

{
    'IsTruncated': True|False,
    'Marker': 'string',
    'NextMarker': 'string',
    'Contents': [
        {
            'Key': 'string',
'''         

    


s3_cli=session.client("s3")

paginator = s3_cli.get_paginator('list_objects')
cnt=1
for each_page in paginator.paginate(
    Bucket="kfsolutions-email"
    ):
        for each_object in  each_page['Contents']:
            print(cnt,each_object['Key']) 
            cnt+=1
            
            #geeft:
            # (1, u'01l3j4r2t1663qvuhgn02c9lhdl26bsvmn6lqoo1')
            # (2, u'03nht8spdsubmt0rsujff7mitc54j15nmqnju081')
            # (3, u'04676r209afuj4mik2062ujriprjj8b75ekji1o1')
            # (4, u'04hu5tqu1q8eq3e19117absg8ujeamtcmnakauo1')
            # ......
            # (2048, u'vvbediinpf1l8mddqjchrn76aepf2armf1uurko1')
            # (2049, u'vvlhcmsqihfu6m6f7uv1n1iqpcl6p5qmpq31ca01')
            # (2050, u'vvulj5q75qf8n7rc774pkinf2bpr3d8st4fovc81')
            
            
