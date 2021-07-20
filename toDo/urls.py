from django.contrib import admin
from django.urls import path, include
from toDo import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet)
router.register(r'groups', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('', include('frontend.urls'))

]



