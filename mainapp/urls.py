from django.urls import path
import mainapp.views


urlpatterns = [
    path("signup/", mainapp.views.SignUp.as_view()),
    path("generate/", mainapp.views.GenerateResults.as_view()),
    path("history/", mainapp.views.GetHistory.as_view())
]