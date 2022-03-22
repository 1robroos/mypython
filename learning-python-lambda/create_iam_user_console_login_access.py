#!/home/linuxbrew/.linuxbrew/bin/python3
# met dit script gaan we met een function de user aan maken 
# de functie is echter te gebruiken om meerdere IAM users aan te maken.

import boto3
from random import choice
import botocore 
import sys 
def get_iam_client_object():
    session=boto3.session.Session(profile_name="kfsoladmin")
    iam_client=session.client(service_name="iam",region_name="us-east-1")
    return iam_client

def get_random_password():
    len_of_password=8
    valid_chars_for_password="ABCDE!@#$%&()abcde12345"
    return "".join(choice(valid_chars_for_password) for each_char in range(len_of_password))


def main():
    iam_client=get_iam_client_object()
    Iam_user_name="1robroos@gmail.com"
    passwrd=get_random_password()
    PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    try:
        iam_client.create_user(UserName=Iam_user_name)
    except Exception as e:
        if e.response['Error']['Code']=="EntityAlreadyExists":
            print("User {} allready exists ".format(Iam_user_name))
            sys.exit(0)
        else:
            print(" Solve this next issue:")
            print(e)
    iam_client.create_login_profile(UserName=Iam_user_name,Password=passwrd,PasswordResetRequired=False)
    iam_client.attach_user_policy(UserName=Iam_user_name,PolicyArn=PolicyArn)
    print("Iam User Name={} and Password = {}".format(Iam_user_name,passwrd))
    return None

if __name__=="__main__":
    main()
    
    
    
# voor mijn account voldoet mijn password niet aan de voorwaarden:
#botocore.errorfactory.PasswordPolicyViolationException: An error occurred (PasswordPolicyViolation) when calling the CreateLoginProfile operation: Password should meet 1 more of the following requirements: Password should have at least one uppercase letter, Password should have at least one symbol

# en als ik he script nog een uit voer: dan krijg ik:
# botocore.errorfactory.EntityAlreadyExistsException: An error occurred (EntityAlreadyExists) when calling the CreateUser operation: User with name 1robroos@gmail.com already exists.