from django.urls import path,re_path
# 匯入 myapp 應用的 views 檔案
from . import views

urlpatterns = [
    path("BadmintonInfo", views.badminton_page)
]