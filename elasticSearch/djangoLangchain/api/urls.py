from django.urls import path
from . import views

urlpatterns = [
  path('chat/', views.chat),
  path('chatgptcsv/', views.langchainCSV),
  path('chatgptsqlite/', views.langchainSqlite),
  # path('chatgptmysql/', views.langchainmysql)
]
