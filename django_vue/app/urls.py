from django.urls import path,re_path
# 匯入 myapp 應用的 views 檔案
from . import views

urlpatterns = [
    re_path(r'add_book$', views.add_book),
    re_path(r'show_books$', views.show_books)
]