from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.


class ListStudents(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

@api_view(['POST'])
def delete_student(request, id):
    user = Student.objects.get(id=id)
    user.delete()
    return Response({'msg': 'student {} deleted successfully'.format(user.student_name)})


@api_view(['POST'])
def update_student(request):
    user = Student.objects.get(id=request.POST.get('student_id'))
    user.student_name = request.POST.get('student_name')
    user.student_intake = Intake.objects.get(id=request.POST.get('student_intake'))
    user.student_track = Track.objects.get(id=request.POST.get('student_track'))
    user.save()
    return Response({'msg': 'student updated successfully'})

