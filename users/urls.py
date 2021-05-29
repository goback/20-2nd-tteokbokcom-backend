from django.urls import path
from users.views import SignUpView, SignInView, KakaoSignInView, MeView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/signin/kakao', KakaoSignInView.as_view()),
    path('/me', MeView.as_view()),
]
