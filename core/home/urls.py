
from django.urls import path
from . views import *

urlpatterns = [
    # path('',home),
    # path('student',post_student),
    # path('student-update/<id>',update_student),
    # path('delete/<id>',delete_student),
    path('book',get_book),
    # path('add-book',add_book)
    path('student/',studentAPI.as_view()),
    path('register/',RegisterUser.as_view()),
    path('generic-student',StudentGenric.as_view()),
    path('generic-ud/<id>',StudentGenric1.as_view())





]
