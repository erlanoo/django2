from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializer, DirectorDetailSerializer, MovieSerializer, MovieDetailSerializer, ReviewSerializer, ReviewDetailSerializer


@api_view(['GET'])
def test_view(request):
    dict_ = {
        'text': 'hello',
        'int': 100,
        'float': 9.99,
        "booleon": True,
        "list": [
            1, 2, 3
        ],
       'dict': {'new': 'yes'}
    }
    return Response(data=dict_)

@api_view(['GET'])
def Directors(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def Directors_detail(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found'},
                        status=404)
    serializer = DirectorDetailSerializer(directors)
    return Response(data=serializer.data)

@api_view(['GET'])
def Movies(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def Movie_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'movie not found'},
                        status=404)
    serializer = MovieDetailSerializer(movie)
    return Response(data=serializer.data)

@api_view(['GET'])
def Reviews(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def Review_detail(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'review not found'},
                        status=404)
    serializer = ReviewDetailSerializer(review)
    return Response(data=serializer.data)