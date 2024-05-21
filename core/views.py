from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import jwt
from dotenv import load_dotenv
import os
from .models import WebUser
from .serializers import WebUserSerializer
from .utility import jwt_required
import json

# Create your views here.
 
# /info，包括进度、用户权限（能否继续实验）、反馈信息、用户实验开始时间、用户的组
@api_view(["GET", "POST"])
@jwt_required
def info(request):
    try:
        sub = request.decoded["sub"]
        webUser = WebUser.objects.get(id=sub)
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
    except WebUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# /writing/[day]，所有的写作（POST、GET)，GET 需要包含参考答案，数据库里面全部用JSON，一张表一个field
@api_view(["GET", "POST"])
@jwt_required
def writing(request, day):
    field_map = {
        '1': 'freeWriting',
        '4': 'challengeWriting1',
        '5': 'challengeWriting2',
        '6': 'challengeWriting3',
        '8': 'virtualLetter',
    }
    try:
        sub = request.decoded["sub"]
        webUser = WebUser.objects.get(id=sub)
        serializer = WebUserSerializer(webUser, context={"writing": True, "field_name": field_map[day]})
        if request.method == "GET":
            if day > webUser.currentDay:
                return Response({"error": f"Current progress has not reach day {day}"}, status=status.HTTP_400_BAD_REQUEST)
            # todo: 对应每一天的参考答案
            with open("writings/challenge_writing_sample.json", "r") as f:
                reference = json.load(f)
            return Response({serializer.data, reference}, status=status.HTTP_200_OK)
        if request.method == "POST":
            # will do word count check at frontend
            if day > int(webUser.currentDay) + 1:
                return Response({"error": f"Current progress has not reach day {day}"}, status=status.HTTP_400_BAD_REQUEST)
            serializer = WebUserSerializer(webUser, data=request.data, partial=True) 
            if serializer.is_valid():
                webUser.currentDay = day
                webUser.save(update_fields=['currentDay'])
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    except WebUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except KeyError:
        return Response({"error": "Invalid day for writing"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
