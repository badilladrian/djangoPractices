"""from .views import *

from django.urls import path, include


urlpatterns = [ 
    path("forms/", forms_list, name="forms_list"),
    path("forms/<int:pk>/", forms_detail, name="forms_detail")
    ]"""

"""
#Now using this library from the restFramework we call the views as follows
urlpatterns = [ 
    path("forms/", FormList.as_view(), name="forms_list"), 
    path("forms/<int:pk>/", FormDetail.as_view(), name="forms_detail"), 
    path("choices/", ChoiceList.as_view(), name="choice_list"), 
    path("input/", CreateInput.as_view(), name="create_input"),
    ]"""

from django.urls import path
from rest_framework.routers import DefaultRouter
from .apiview import *

router = DefaultRouter() 
router.register('forms', FormViewSet)

#The new nested structure
urlpatterns = [ 
    path("forms/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"), 
    path("forms/<int:pk>/choices/<int:choice_pk>/input/", CreateInput.as_view(), name="create_input"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"), 
]

urlpatterns += router.urls