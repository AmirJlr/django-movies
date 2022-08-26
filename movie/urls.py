from django.urls import path, re_path
from .views import home, detail ,createReview,updateReview, deleteReview

app_name = 'movie'

urlpatterns = [
    path('', home, name='home'),
    path('movies/<int:movie_id>/', detail, name='detail'),
    
    path('<int:movie_id>/create-review', createReview, name='createreview'),
    path('<int:review_id>/update-review', updateReview, name='updatereview'),
    path('<int:review_id>/delete-review', deleteReview, name='deletereview'),
]
