
from django.contrib import admin
from stolovka import views as stolovka_views
from django.urls import include, path
# from rest_framework import routers
from rest_framework_nested import routers #создание многоуровневых путей


router = routers.DefaultRouter()
router.register(r'food', stolovka_views.FoodViewSet)
#router.register(r'type', stolovka_views.FoodTypeViewSet)
router.register(r'dorm', stolovka_views.DormViewSet)

list_router=routers.DefaultRouter()
list_router.register(r'list', stolovka_views.FoodTypeViewSet)

menu_router=routers.NestedDefaultRouter(list_router, r'list', lookup='list')
menu_router.register(r'menu', stolovka_views.MenuViewSet, basename='menu')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(list_router.urls)),
    path('', include(menu_router.urls)),
    path('admin/', admin.site.urls),

]
