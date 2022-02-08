from django.urls import path,include
from students.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'^list_students', ListStudents)

urlpatterns = [
    path('', include(router.urls)),
    path('delete_student/<id>', delete_student),
    path('update_student', update_student),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
