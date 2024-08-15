from django.http import JsonResponse
from functools import wraps
import jwt
from rest_framework import status
from dotenv import load_dotenv
import os
import django
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode

sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'CPTBackend.settings'
django.setup()

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

def getEncryptedPhoneNumberFromRequest(request)->str:
    token = request.headers['Authorization'][7:]
    decoded = jwt.decode(token, options={"verify_signature": False})
    phoneNumber = decoded['username']
    return phoneNumber



key = b64decode(os.getenv('AES_KEY'))
def encryptPhoneNumber(plaintext):
    while len(plaintext) % 16 != 0:
        plaintext += ' '  # Padding with spaces

    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext.encode('utf-8')) + encryptor.finalize()
    print(b64encode(ct).decode('utf-8') )
    return b64encode(ct).decode('utf-8') 

def decryptPhoneNumber(ciphertext):
    ct = b64decode(ciphertext)
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ct) + decryptor.finalize()
    return decrypted_data.decode('utf-8').strip() 

