from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import People, Book
from home.serializers import PeopleSerializer, BookSerializer, loginSerializer


@api_view(['GET','POST','PUT'])
def login(request):
    data = request.data
    serializer = loginSerializer(data=data)
    if serializer.is_valid():
        data = serializer.validated_data
        return Response(f"Login Successful for {data['email']}")
    return Response(serializer.errors)

@api_view(['GET','POST','PUT'])
def index(request):
    courses ={
            'course_name':'Python',
            'learn':['Django','Flask','FastAPI'],
            'course_provider':'youtube'
        }
    if request.method=='GET':     
        search = request.GET.get('search')
        print(search)   
        print('This is a get request')
        return Response(courses)
    elif request.method=='POST':
        data = request.data
        print(data)
        print('This is a post request')
        return Response(courses)
    elif request.method=='PUT':
        print('This is a put request')
        return Response(courses)



@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])    
def people(request):
    if request.method=='GET':     
        obj = People.objects.all()
        # return Response(obj)
        serializer = PeopleSerializer(obj, many=True)
        return Response(serializer.data)
        # return Response("This is GET request for People")
    elif request.method=='POST':
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method=='PUT':
        data = request.data
        serializer = PeopleSerializer( data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method=='PATCH':
        data = request.data
        person_obj = People.objects.get(id=data['id'])
        serializer = PeopleSerializer(person_obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors)
    elif request.method=='DELETE':
        data = request.data
        person_obj = People.objects.get(id=data['id'])
        person_obj.delete()
        return Response("Deleted Successfully")

@api_view(['GET','POST','PUT'])        
def book(request):
    if request.method=='GET':
        obj = Book.objects.all()
        serializer = BookSerializer(obj, many=True)
        return Response(serializer.data)
    if request.method=='POST':
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    # if request.method=='PUT':
    #     data = request.data
    #     book_id = data.get('id')
    #     obj = Book.objects.get(id=book_id)
    #     serializer = BookSerializer(obj, data=data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)