from django.urls import path
from .views import load_frontend, submit_prompt  # Import both views

app_name = 'main'

urlpatterns = [
    path("", load_frontend, name="frontend"),         # For loading the homepage
    path("submit-prompt/", submit_prompt, name="submit_prompt"),  # For handling form submission
]
