from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from movie.models import Movies, Ratings
import json
# Create your views here.
@csrf_exempt
def selectMovie(request):
    if request.method == "POST":
        request_body = json.loads(request.body.decode('utf-8'))
        movie_id = request_body['movie_id']
        movie_info = Movies.objects.filter(movie_id=int(movie_id))

        movie_list = []
        print(len(movie_info))
        for index in range(0,len(movie_info)):
            index = int(index)
            data = {
                "movie_id": movie_info[index].movie_id,
                "title": movie_info[index].title,
                "genres": movie_info[index].genres
            }
        movie_list.append(data)
        print(movie_list)
        return JsonResponse({"movie_list": movie_list})
    else:
        return HttpResponse("wrong method@@")

def getMovieByUserID(request):
	user_id=request.GET['user_id']
	user_info= Ratings.objects.filter(user_id=int(user_id))
	movie_list=[]
	for index in range(0,len(user_info)):
		index= int(index)
		data={
			"movie_id": user_info[index].movie_id
		}
		movie_list.append(data)
	return JsonResponse({"movie_list": movie_list})

def insertData(request):
	user=request.GET['user_id']
	movie=request.GET['movie_id']
	rate=request.GET['rating']
	rating_data=Ratings(user_id=user,movie_id=movie,rating=rate)
	rating_data.save()
	user_info= Ratings.objects.filter(user_id=int(user))
	movie_list=[]
	for index in range(0,len(user_info)):
		index= int(index)
		data={
			"user_id" : user_info[index].user_id,
			"movie_id": user_info[index].movie_id,
			"rating" : user_info[index].rating
		}
		movie_list.append(data)
	return JsonResponse({"movie_list": movie_list})

def deleteData(request):
	user=request.GET['user_id']
	movie=request.GET['movie_id']
	Ratings.objects.filter(user_id=int(user), movie_id=int(movie)).delete()
	user_info= Ratings.objects.filter(user_id=int(user))
	movie_list=[]
	for index in range(0,len(user_info)):
		index= int(index)
		data={
			"user_id" : user_info[index].user_id,
			"movie_id": user_info[index].movie_id,
			"rating" : user_info[index].rating
		}
		movie_list.append(data)
	return JsonResponse({"movie_list": movie_list})
def updateData(request):
	user=request.GET['user_id']
	movie=request.GET['movie_id']
	rate=request.GET['rating']
	Ratings.objects.filter(user_id=int(user), movie_id=int(movie)).update(rating=float(rate))
	user_info= Ratings.objects.filter(user_id=int(user))
	movie_list=[]
	for index in range(0,len(user_info)):
		index= int(index)
		data={
			"user_id" : user_info[index].user_id,
			"movie_id": user_info[index].movie_id,
			"rating" : user_info[index].rating
		}
		movie_list.append(data)
	return JsonResponse({"movie_list": movie_list})

def userData(request):
	if request.method == 'GET':
		movie_list=[]
		return render(request,'record.html', {'movie_list': movie_list})
	else :
		user=request.POST.get('user_id')
		print("user",user)
		user_info=Ratings.objects.filter(user_id=int(user))
		movie_list=[]
		for index in range(0,len(user_info)):
			index=int(index)
			data ={
				"movie_name" : user_info[index].movie_id,
				"rating" : user_info[index].rating
			}
			movie_list.append(data)
	return render(request,'record.html', {'movie_list': movie_list})