from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import users, colleges 
from django.http import HttpResponse
import json, requests

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def createUser(request):
    if request.method == 'POST':
        userRow = users.objects.create(
            username = json.loads(request.body)["username"], 
            password = json.loads(request.body)["password"],
            role =  json.loads(request.body)["role"] 
        )
        return HttpResponse('created user successfully')

@csrf_exempt
def retrieveUsers(request):
    if request.method == 'GET':
        usersData = users.objects.all()
        usersList= []
        for user in usersData:
            userData = {}
            userData['id'] = user.id
            userData['username'] = user.username
            userData['password'] = user.password
            userData['role'] = user.role
            usersList.append(userData)
        return HttpResponse(json.dumps(usersList))


@csrf_exempt
def updateUser(request):
    if request.method == 'POST':
        usersData = users.objects.filter(
            id = json.loads(request.body)["id"]
            ).update(
            username = json.loads(request.body)["username"], 
            password = json.loads(request.body)["password"],
            role =  json.loads(request.body)["role"]
            )
        return HttpResponse('user updated successfully')

@csrf_exempt
def deleteUser(request):
    if request.method == 'POST':
        usersData = users.objects.filter(
            id = json.loads(request.body)["id"]
            ).delete()
        return HttpResponse('user deleted successfully')


@csrf_exempt
def createCollege(request):
    if request.method == 'POST':
        collegesRow = colleges.objects.create(
            name = json.loads(request.body)["name"], 
            year = json.loads(request.body)["year"],
            location =  json.loads(request.body)["location"],
            courses = json.loads(request.body)["courses"],
            strength = json.loads(request.body)["strength"],
            admission = json.loads(request.body)["admission"]
        )
        return HttpResponse('created college successfully')

@csrf_exempt
def retrieveColleges(request):
    if request.method == 'GET':
        collegesData = colleges.objects.all()
        collegesList= []
        for college in collegesData:
            collegeData = {}
            collegeData['id'] = college.id
            collegeData['name'] = college.name
            collegeData['year'] = college.year
            collegeData['location'] = college.location
            collegeData['courses'] =  college.courses 
            collegeData['strength'] = college.strength
            collegeData['admission'] = str(college.admission)
            collegesList.append(collegeData)
        return HttpResponse(json.dumps(collegesList))    



@csrf_exempt
def updateCollege(request):
    if request.method == 'POST':
        collegesData = colleges.objects.filter(
            id = json.loads(request.body)["id"]
            ).update(
            name = json.loads(request.body)["name"],
            year = json.loads(request.body)["year"],
            location =  json.loads(request.body)["location"],
            courses = json.loads(request.body)["courses"],
            strength = json.loads(request.body)["strength"],
            admission = json.loads(request.body)["admission"]
            )
        return HttpResponse('college details updated successfully')

@csrf_exempt
def deleteCollege(request):
    if request.method == 'POST':
        collegesData = colleges.objects.filter(
            id = json.loads(request.body)["id"]
            ).delete()
        return HttpResponse('college detials deleted successfully')
