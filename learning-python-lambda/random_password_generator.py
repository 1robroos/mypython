from random import choice

# length of password
len_of_password=8

# valid characters for password:
valid_chars_for_password="abcde12345"

print choice(valid_chars_for_password)
# geeft bijvoorbeeld "d"
# choice is een method van random die een willekeurige karakter uit je string pakt.


# we hebben 8 karakters nodig. Laten we simpel een list maken:
password=[]
print("waarde password list is ", password)  # geeft : ('waarde password list is ', [])
for each_password_char in range(len_of_password):
    print choice(valid_chars_for_password)
# geeft bijv:
# 2
# e
# c
# d
# 1
# 4
# 5
# b
# a

# je krijgt steeds verschillende letters.
# choice is een method van random die willekeurige letters pakt uit valid_chars_for_password
#nu appenden:
    
for each_password_char in range(len_of_password):
    password.append(choice(valid_chars_for_password))
    
print(password)
# dit geeft een list : ['4', '3', '4', '1', '5', '3', '4', '5']

# met join method gooi je het in 1 string:

print("".join(password))
# geeft : 43415345

#Gooi dit in een var:
random_pass="".join(password)
print(random_pass)
# geeft : 43415345
   
   
# dit kan ook korter:
random_pass="".join(choice(valid_chars_for_password) for each_char in range(len_of_password))
print(random_pass)
# je haalt willekeurige karakters op voor de lengte van je voorgedefinieerde password list , en join die dan.
 