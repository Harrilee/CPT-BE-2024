from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import jwt
from dotenv import load_dotenv
import os
from .models import WebUser
from .serializers import WebUserSerializer

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

# Create your views here.

# /info，包括进度、用户权限（能否继续实验）、反馈信息、用户实验开始时间、用户的组
@api_view(["GET", "POST"])
def info(request):
    try:
        # temporary decoder here, simple_jwt requires "id" and "exp"
        token = request.headers['Authorization'][7:]
        decoded = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        print(decoded)
        if "name" not in decoded or "sub" not in decoded:
            return Response({"error": "Missing required claim name or sub"}, status=status.HTTP_400_BAD_REQUEST) 
        name = decoded["name"]
        sub = decoded["sub"]
        webUser = WebUser.objects.get(sub=sub, name=name)
        serializer = WebUserSerializer(webUser, context={"info": True})
        if request.method == "GET":
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == "POST":
            serializer = WebUserSerializer(webUser, data=request.data, partial=True) 
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    except jwt.ExpiredSignatureError:
        return Response({'error': 'Token expired'}, status=status.HTTP_401_UNAUTHORIZED)
    except jwt.DecodeError:
        return Response({'error': 'Error decoding token'}, status=status.HTTP_401_UNAUTHORIZED)
    except WebUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
