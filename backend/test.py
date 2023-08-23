import jwt

encoded_jwt = jwt.encode({'id':'1',"name":"John"},'secret',algorithm='HS256')

print(encoded_jwt)

dedcoded = jwt.decode(encoded_jwt,'secret',algorithms=['HS256'])

print(dedcoded)