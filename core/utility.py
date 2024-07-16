from django.http import JsonResponse
from functools import wraps
import jwt
from rest_framework import status
from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()

# temporary decoder here, simple_jwt requires "id" and "exp"
def jwt_required(f):
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        try:
            token = request.headers.get('Authorization', '')
            if not token:
                return JsonResponse({'error': 'Authorization token is missing'}, status=status.HTTP_401_UNAUTHORIZED)
            decoded = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
            if "name" not in decoded or "sub" not in decoded:
                return JsonResponse({"error": "Missing required claim name or sub"}, status=status.HTTP_400_BAD_REQUEST)

            request.decoded = decoded
            return f(request, *args, **kwargs)
        
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token expired'}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.DecodeError:
            return JsonResponse({'error': 'Error decoding token'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return decorated_function

usernameEncryptionSalt = int(os.getenv("ENCRYPTION_SALT")) # same as in frontend
# awsClient = boto3.client(
#     'logs', 
#     aws_access_key_id='AKIAXKF6HT3IEUTQVWW5',
#     aws_secret_access_key="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",
#     region_name='ap-east-1'
# )

def getEncryptedPhoneNumberFromRequest(request)->str:
    token = request.headers['Authorization'][7:]
    decoded = jwt.decode(token, options={"verify_signature": False})
    phoneNumber = decoded['username']
    return phoneNumber

def encryptPhoneNumber(phoneNumber: str)->str:
    usernameInt = int(phoneNumber) - 10000000000
    usernameInt -= usernameEncryptionSalt
    encryptedUsername = np.base_repr(usernameInt, 36)
    return encryptedUsername

def decryptPhoneNumber(userId: str)->str:
    base10 = int(userId, 36)
    base10 += usernameEncryptionSalt
    base10 += 10000000000
    return str(base10)

# def cloudWatchPutLogEvents(userId: str, eventName: str, url: str, value: str):
#     response = awsClient.put_log_events(
#         logGroupName='CPT',
#         logStreamName='default',
#         logEvents=[{
#             'timestamp': int(time.time()*1000),
#             'message': json.dumps({
#                 'userId': userId,
#                 'eventName': eventName,
#                 'url': url,
#                 'value': value
#             })
#         }])
#     return response

if __name__ == '__main__':
    print(encryptPhoneNumber("18908133815"))
    print(decryptPhoneNumber('balabala'))