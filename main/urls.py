from django.urls import path
from .views import index
from .views import other_page
from .views import BBLoginView
from .views import profile
from .views import BBLogoutView
from .views import ChangeUserInfoView
from .views import BBPasswordChangeView
from .views import RegisterDoneView, RegisterUserView
from .views import user_activate
from .views import DeleteUserView


app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('<str:page>/', other_page, name='other'),
    path('account/login', BBLoginView.as_view(),name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('account/logout/', BBLogoutView.as_view(), name='logout'),
    path('account/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),

]


