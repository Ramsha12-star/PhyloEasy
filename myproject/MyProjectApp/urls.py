from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.hi, name="home-page"),
    path('Tutorials/', views.Tutorials, name="Tutorials"),
    path('About/', views.About, name="About"),
    path('Contactpg/', views.Contactpg, name="Contactpg"),
    path('xyz/', views.xyz, name="xyz"),
    path('downloadpy1/', views.download_file, name="Download1"),
	path('downloadpy2/', views.download_file2, name="Download2"),
	path('downloadpy3/', views.download_file3, name="Download3"),
    path('downloadpy4/', views.download_file4, name="Download4"),
    path('downloadpy5/', views.download_file5, name="Download5"),
    path('downloadpy6/', views.download_file6, name="Download6"),
   path('downloadpy7/', views.download_file7, name="Download7"),
   path('downloadpy8/', views.download_file8, name="Download8"),
   path('downloadpy9/', views.download_file9, name="Download9"),
   path('download_image/', views.download_image, name="download_image"),
  path('download_image1/', views.download_image1, name="download_image1"),
  path('download_image2/', views.download_image2, name="download_image2"),
   path('send', views.send),
  
   
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
