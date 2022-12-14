from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('all_content_api',views.ContentModelViewSet,basename="Content")
router.register('top_10',views.Top10ContentModelViewSet,basename="Top10Content")
router.register('top_5',views.Top5ContentModelViewSet,basename="Top5Content")
router.register('top_3',views.Top3ContentModelViewSet,basename="Top3Content")

from . import views
urlpatterns = [
    path('api/',include(router.urls),name = "Show All Content"),
   
]
