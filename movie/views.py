from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Review
from .forms import ReviewForm

from django.contrib.auth.decorators import login_required
# Create your views here.

# home page for listing movies


def home(request):
    searchTerm = request.GET.get('SearchMovie') or ''
    if searchTerm is not None:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()

    context = {
        'searchTerm': searchTerm,
        'movies': movies,

    }
    return render(request, 'movie/home.html', context)
 

# Detail page for each movie
def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    reviews = Review.objects.filter(movie=movie)

    return render(request, 'movie/detail.html',
                  {'movie': movie, 'reviews': reviews})


# create comments in detail page
@login_required
def createReview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'GET':
        return render(request, 'movie/createreview.html', {'form': ReviewForm})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)

            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('movie:detail', newReview.movie.id)
        except ValueError:
            return render(request, 'movie/createreview.html',
                          {'form': ReviewForm(), 'error': 'bad data pass in'})


@login_required
def updateReview(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'movie/updatereview.html', {'review': review, 'form': form})

    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('movie:detail', review.movie.id)
        except ValueError:
            return render(request, 'movie/updatereview.html',
                          {'review': review, 'form': form, 'error': 'Bad data in form'})

@login_required
def deleteReview(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    return redirect('movie:detail',review.movie.id)
