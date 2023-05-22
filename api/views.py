from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
# Create your views here.
# This views file will create all of the routes for the application

def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note'
        },
         {
            'Endpoint': '/notes/create',
            'method': 'POST',
            'body': {"body": ""},
            'description': 'Create a new note with data sent'
        },
        {
            'Endpoint': '/notes/id/update',
            'method': 'PUT',
            'body': {"body": ""},
            'description': 'Updates an existing note'
        },
        {
            'Endpoint': '/notes/id/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exits note'
        }
    ]

    # safe = False allows us to return more types of data rather than just dictionaries
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    # many = True, which means that this will serialize multiple objects
    serializer = NoteSerializer(notes, many=True)
    # serializer is going to be an object and we just want the data
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, p):
    notes = Note.objects.get(id=p)
    # many = True, which means that this will serialize just one object
    serializer = NoteSerializer(notes, many=False)
    # serializer is going to be an object and we just want the data
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request, p):
    data = request.data 

    note = Note.objects.get(id=p)

    serializer = NoteSerializer(instance=note, many=False, data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, p):
    note = Note.objects.get(id=p)
    note.delete()

    return Response("Delete successfully")

@api_view(['POST'])
def createNote(request):
    data = request.data 
    note = Note.objects.create(
        body = data['body']
    )

    serializer = NoteSerializer(note, many=False)

    # if serializer.is_valid():
    #     serializer.save()

    return Response(serializer.data)