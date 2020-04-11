from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("user.urls")),
    path('api/', include('api.urls')),
    path('seminar/', include('seminars.urls')),
    path('', include('blog.urls')),
]

# Error Pages urls
# handler400 = 'error_pages.views.error_404'
# handler500 = 'error_pages.views.error_500'


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
