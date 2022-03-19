'''
import sys
try:
    import boto3e
except Exception as e:
    print(e)
    
import boto3

print(dir(boto3))

print(dir(boto3.exceptions))

try:
    import xyz
# except ModuleNotFoundError:
#     print("xyz kan ik niet inleze als module")
# except Exception as e:
#     print(e)    
'''

'''
import sys
import dtcd
try:
    import xyz
except ImportError:
    print("lukt niet vandaag")
    sys.exit(1)
except Exception as e:
    print(e)
    sys.exit(1)
    
print("we gaan verder")
'''

# try:
#     import boto3
#     import botocore
#     import sys
# except Exception as e:
#     print(e)
# try:
#     aws_mag_con=boto3.session.Session(profile_name="techie")
# except botocore.exceptions.ProfileNotFound:
#     print("profile techie bestaat niet")
#    sys.exit(3)



try:
    import boto3
    import botocore
    import sys
    from pprint import pprint
except Exception as e:
    print(e)
try:
    aws_mag_con=boto3.session.Session(profile_name="lambda_upload")
except botocore.exceptions.ProfileNotFound:
    print("profile  lambda-upload bestaat niet")
    sys.exit(3)
try:
    iam_con_re=aws_mag_con.resource(service_name="iam")
    for each_user in iam_con_re.users.all():
        print(each_user)
except botocore.exceptions.ClientError as e:
    #print(dir(e))
    #pprint(e.response['Error']['Code'])
    if e.response['Error']['Code']=="AccessDenied":
        print("Your profile has no access to IAM ")
    else:
        print(e.response['Error']['Code'])
    
except Exception as e:
    print(e)
    sys.exit(5)