from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

users={}

@csrf_exempt
def user_view(request,user_id=None):
    if request.method=="GET":
        if user_id:
            user=users.get(user_id)
            if user:
                return JsonResponse(user)
            return JsonResponse({"error":"user not found"},status=404)
        return JsonResponse(users)
    
    elif request.method=="POST":
        data=json.loads(request.body)
        user_id=str(len(users)+1)
        users[user_id]=data
        return JsonResponse({"id":user_id,"message":"User created"},status=201)
    
    elif request.method=="PUT" and user_id:
        if user_id in users:
            data=json.loads(request.body)
            users[user_id].update(data)
            return JsonResponse({"message":"User updated"})
        return JsonResponse({"error":"User not found"},status=404)
    
    elif request.method=="DELETE" and user_id:
        if user_id in users:
            del users[user_id]
            return JsonResponse({"message":"User deleted"})
        return JsonResponse({"error":"User not found"},status=404)
