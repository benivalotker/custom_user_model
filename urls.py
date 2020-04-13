from django.urls import path
from .views import login_, logout_, register_

urlpatterns = [
    path('', login_, name="users_login"),
    path('register/', register_, name="users_register"),
    path('logout/', logout_, name="users_logout"),
]
