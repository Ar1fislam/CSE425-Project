
from django.urls import include, path
from rest_framework import routers
from .views import NewsModelViewSet

router = routers.DefaultRouter()
router.register(r'news', NewsModelViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]