import boto3
import datetime
import sys
import botocore

session=boto3.session.Session(profile_name="kfsoladmin")
iam_con_re=session.resource(service_name="iam")
'''
# Get Details of any IAM user.
iam_user_ob=iam_con_re.User("lambda-upload")
print(dir(iam_user_ob))
print(iam_user_ob.user_name,iam_user_ob.create_date.strftime("%Y-%m-%d"))
'''

# Now work with multiple users.

# for iam_user_ob in iam_con_re.users.all():
#     print(iam_user_ob)
#     print(iam_user_ob.user_name,iam_user_ob.create_date.strftime("%Y-%m-%d"))
'''
try:
    filter_users={"Name":"create_date","Values":["2018-07-11"]}
    for iam_user_ob in iam_con_re.users.filter(Filters=[filter_users]):
        print(iam_user_ob)
        print(iam_user_ob.user_name,iam_user_ob.create_date.strftime("%Y-%m-%d"))
except botocore.exceptions.ParamValidationError:
    print("Filter", filter_users,"  is niet toepasbaar op users object als filter.")
    sys.exit(3)
except Exception as e:
    print(e.message)
    print(dir(e))
# #filter error:
# botocore.exceptions.ParamValidationError: Parameter validation failed:    <== een botocore exception !
# Unknown parameter in input: "Filters", must be one of: PathPrefix, Marker, MaxItems
# ParamValidationError is een exception in botocore.exceptions
'''


try:
    for iam_user_ob in iam_con_re.users.limit(count=3):
        print(iam_user_ob)
        print(iam_user_ob.user_name,iam_user_ob.create_date.strftime("%Y-%m-%d"))
except botocore.exceptions.ParamValidationError:
    print("Filter", filter_users,"  is niet toepasbaar op users object als filter.")
    sys.exit(3)
except Exception as e:
    print(e.message)