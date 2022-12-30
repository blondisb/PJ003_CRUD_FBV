from django.urls import path
from . import views as vw

urlpatterns = [
    path('', vw.VW_home, name='URL_home'),
    path('about/', vw.VW_about, name='URL_about'),
    path('projects/', vw.VW_project_list, name='URL_projects'),
    path('emptytable/', vw.VW_empty_table, name='URL_empty_table'),
    path('tasks/<int:id_tsk>', vw.VW_task, name='URL_tasks'),
    path('tasks2/', vw.VW_task2, name='URL_tasks2'),
    path('addtasks/', vw.VW_addtask, name='URL_addtasks'),
    path('addprojects/', vw.VW_addproject, name='URL_addprojects'),
    path('projectdetails/<int:id_pj>', vw.VW_projectdetails, name='URL_projectdetails'),
]
