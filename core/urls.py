from django.urls import path
from .views import PublicNoteListView, ProtectedNoteCreateView , UserSignupView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('public/notes/', PublicNoteListView.as_view(), name='public-notes'),
    path('protected/notes/', ProtectedNoteCreateView.as_view(), name='protected-notes'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refersh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
