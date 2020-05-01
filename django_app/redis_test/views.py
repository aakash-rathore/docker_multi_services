from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import redis
import json

# Create your views here.
@api_view(["POST"])
def add_user(request):
    data = json.loads(request.body.decode("utf-8"))
    api_response = {}
    try:
        r = redis.Redis.from_url("redis://localhost:6379/0")
        r.set("firstname", data["firstname"])
        r.set("lastname", data["lastname"])
        api_response["message"] = "success"
        return Response(api_response, status=201)
    except:
        api_response["message"] = "Failed"
        return Response(api_response, status=500)


@api_view(["GET"])
def get_user(request):
    api_response = {}
    try:
        r = redis.Redis.from_url("redis://localhost:6379/0")
        f_name = r.get("firstname")
        l_name = r.get("lastname")
        api_response["message"] = "success"
        api_response["First_Name"] = f_name
        api_response["Last_Name"] = l_name
        return Response(api_response, status=200)
    except:
        api_response["message"] = "Failed"
        return Response(api_response, status=500)
