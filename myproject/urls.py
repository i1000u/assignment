from django.contrib import admin
from django.urls import path, include
import myapp.views
from django.conf import settings
from django.conf.urls.static import static


# from xml.etree.ElementInclude import include
# from django.contrib import admin
# from django.urls import path
# import myapp.views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.main, name='main'),
    path('write/', myapp.views.write, name='write'),
    path('read/', myapp.views.read, name='read'),
    path('detail/<str:id>/', myapp.views.detail, name='detail'),
    path('edit/<str:id>/', myapp.views.edit, name='edit'),
    path('delete/<str:id>/', myapp.views.delete, name='delete'),
    path('hashtag/', myapp.views.hashtag, name='hashtag'),
    path('', include('accounts.urls')),
    # path('', include('myproject.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
