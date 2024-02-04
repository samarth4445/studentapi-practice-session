from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def student(request):
    students = Student.objects.all() # SELECT * FROM Student
    # student = Student.objects.get(id=3) # SELECT * FROM Student WHERE id=2 (For getting only one row)
    # student = Student.objects.filter(batch_name="A") # SELECT * FROM WHERE batch_name='A' (For getting multiple rows which match the query)

    student_list = []

    for student in students:
        student_data = {
            "name": student.name,
            "roll_number": student.roll_number,
            "batch_name": student.batch_name,
            "class_name": student.class_name,
        }

        student_list.append(student_data)

    return JsonResponse({
        'students': student_list
    })

@csrf_exempt
def student_create(request):
    if request.method == "POST":
        student_data = json.loads(request.body)
        
        Student.objects.create(                 # INSERT INTO Student VALUES(name, roll ....)
            name=student_data['name'],
            roll_number=student_data['roll_number'],
            class_name=student_data['class_name'],
            batch_name=student_data['batch_name'],
        )                                
        
    return JsonResponse({
        'message': 'Student has been created!'
    })