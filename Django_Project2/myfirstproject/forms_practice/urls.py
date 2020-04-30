from django.urls import path
from . import views

urlpatterns=[
    path('',views.detail,name='detail'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    # path('show',views.show,name='show')
]