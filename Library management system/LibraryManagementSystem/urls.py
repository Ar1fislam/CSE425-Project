from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework import routers
# from api.views import NewsModelViewSet
# from api.views import news_list

# router = routers.DefaultRouter()
# # router.register(r'news', NewsModelViewSet)
# router.register(r'news', NewsModelViewSet, basename='news')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls')),
    path('api/', include('api.urls')),
    # path('api/news/', news_list),
    # path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
