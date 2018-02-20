from django.shortcuts import render, HttpResponse, redirect
from models import *
from sets import Set

def index(request):
    all_users = User.objects.all()
    all_friends = Friendship.objects.all() 
    friendships = []
    for friends in all_friends:
        friendships.append(str(all_users.get(id=friends.friend_friend_id).name) + "->" + str(all_users.get(id=friends.user_friend_id).name))
    allusers = {
        'users' : User.objects.all(),
        'friendships': friendships
    }
    return render(request, 'friends_app/index.html', allusers)

def register(request):
    User.objects.create(name = request.POST['name'])
    return redirect('/')

def add_friend(request):
    user = User.objects.get(id=request.POST['useradd'])
    friend = User.objects.get(id=request.POST['friendadd'])
    Friendship.objects.create(user_friend = user, friend_friend = friend)
    return redirect('/')

def check_friends(request):
    currentfriends = Set([])
    allusers = Set([])
    all_users = User.objects.all()
    all_friendships = Friendship.objects.all() 
    for friendship in all_friendships:
        if friendship.user_friend_id == int(request.POST['checkfriend']):
            currentfriends.add(User.objects.get(id = friendship.friend_friend_id).name)
        if friendship.friend_friend_id == int(request.POST['checkfriend']):
            currentfriends.add(User.objects.get(id = friendship.user_friend_id).name)
    for user in all_users:
        if not user.name == User.objects.get(id = request.POST['checkfriend']).name:
            allusers.add(user.name)
    print currentfriends
    all = {
        'name': User.objects.get(id=request.POST['checkfriend']).name,
        'currentfriends' : currentfriends,
        'notfriends' : allusers.difference(currentfriends)
    }
    return render(request,'friends_app/checkfriends.html', all)
