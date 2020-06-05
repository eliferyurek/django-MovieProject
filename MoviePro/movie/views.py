import json
import psycopg2
import csv

from django.shortcuts import render, redirect
from .forms import *

from django.http import JsonResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .decorators import unauthenticated_user, admin_only


# Create your views here.



@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')


            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
                username=user.username,
                email=user.email,
            )

            messages.success(request, 'Account was created successfully for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'movie/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Please check your password and username')

    context = {}
    return render(request, 'movie/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    customers = Customer.objects.all()

    movies = Movie.objects.all()

    stores = Store.objects.all()

    orders = MovieOrder.objects.all()

    directors = Director.objects.all()

    actors = Actor.objects.all()

    context = {'customers': customers, 'movies': movies, 'stores': stores, 'orders': orders, 'directors': directors,
               'actors': actors}

    return render(request, 'movie/dashboard.html', context)


@login_required(login_url='login')
def userPage(request):
    context = {}
    return render(request, 'movie/user.html', context)


@login_required(login_url='login')
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your information has been updated.')
            return redirect('movies')

    context = {'form': form, 'customer': customer}
    return render(request, 'movie/settings.html', context)


@login_required(login_url='login')
def movie(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.movieorder_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}

    movies = Movie.objects.all()

    context = {'movies': movies}

    return render(request, 'movie/movies.html', context)


@login_required(login_url='login')
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    return render(request, 'movie/customer.html', {'customer': customer})


def cart(request):
    if request.user.is_authenticated:
        customer1 = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer1, complete=False)
        items = order.movieorder_set.all()
        stores = Store.objects.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}

    context = {'items': items, 'order': order, 'stores': stores}
    return render(request, 'movie/cart.html', context)


def createMovie(request):
    form = CreateMovieForm()
    if request.method == 'POST':
        form = CreateMovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'movie/createMovie.html', context)


def movieView(request, pk_movie):
    movie = Movie.objects.get(id=pk_movie)

    context = {'movie': movie}
    return render(request, 'movie/movie_view.html', context)


def updateMovie(request, pk_movie):
    movie = Movie.objects.get(id=pk_movie)
    form = CreateMovieForm(instance=movie)

    if request.method == 'POST':
        form = CreateMovieForm(request.POST, request.FILES,  instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'movie': movie, 'form': form}
    return render(request, 'movie/createMovie.html', context)


def deleteMovie(request, pk_movie):
    movie = Movie.objects.get(id=pk_movie)

    if request.method == "POST":
        movie.delete()
        return redirect('/')

    context = {'delete_movie': movie}
    return render(request, 'movie/deleteMovie.html', context)


def createCustomer(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')

            Customer.objects.create(
                user=user,
                username=user.username,
                email=user.email,
            )

            messages.success(request, 'Account was created successfully for ' + username)
            return redirect('/')

    context = {'form': form}
    return render(request, 'movie/createCustomer.html', context)


def updateCustomer(request, pk_customer):
    customer = Customer.objects.get(id=pk_customer)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'customer': customer}
    return render(request, 'movie/settings.html', context)


def deleteCustomer(request, pk_customer):
    customer = Customer.objects.get(id=pk_customer)

    if request.method == "POST":
        customer.delete()
        return redirect('/')

    context = {'delete_customer': customer}
    return render(request, 'movie/deleteCustomer.html', context)


def addressCustomer(request):
    if request.user.is_authenticated:
        customer1 = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer1, complete=False)
        items = order.movieorder_set.all()
        form = AddressForm()
        if request.method == 'POST':
            form = AddressForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}

    context = {'items': items, 'order': order, 'form': form, 'customer': customer1}
    return render(request, 'movie/address.html', context)


def updateCart(request):
    conn = psycopg2.connect(host="localhost", user="postgres", password="elif2568940", dbname="movieDB")
    cur = conn.cursor()

    data = json.loads(request.body)
    movieID = data['movieID']
    action = data['action']

    print('Action:', action)
    print('movieID', movieID)

    customer = request.user.customer
    movie = Movie.objects.get(id=movieID)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    movieOrder, created = MovieOrder.objects.get_or_create(order=order, movie=movie)

    if action == 'add':
        #if movieOrder.quantity < movie.inventory.inventory:
        movieOrder.quantity = (movieOrder.quantity + 1)
        cur.execute("UPDATE movie_movie set inventory_id = inventory_id - 1 where id = %s", movieID)
        conn.commit()
        if movie.inventory.inventory == 1:
            messages.warning(request, "There is not in the stock or in someone else's cart...")

    elif action == 'remove':
        movieOrder.quantity = (movieOrder.quantity - 1)
        cur.execute("UPDATE movie_movie set inventory_id = inventory_id + 1 where id = %s", movieID)
        conn.commit()


    movieOrder.save()

    if movieOrder.quantity <= 0:
        movieOrder.delete()

    return JsonResponse('It was added to the cart...', safe=False)


def processOrder(request):
    data = json.loads(request.body)

    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    total = float(data['form']['total'])

    if total == order.get_cart_total:
        order.complete = True


    order.save()

    if order.shipping == True:
        AddressCustomer.objects.create(
            customer=customer,
            order=order,
            addres=data['shipping']['address'],
            city=data['shipping']['city'],
        )

    return JsonResponse('Payment complete...', safe=False)


@login_required(login_url='login')
def store(request):
    dropdown = request.GET['dropdown1']

    store = Store.objects.all()

    context = {'dropdown1': dropdown, 'store': store}
    return render(request, 'movie/store.html', context)


def addStore(request):
    form = StoreForm()
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'movie/addStore.html', context)


def updateStore(request, pk_store):
    store = Store.objects.get(id=pk_store)
    form = StoreForm(instance=store)

    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'movie/addStore.html', context)


def deleteStore(request, pk_store):
    store = Store.objects.get(id=pk_store)

    if request.method == "POST":
        store.delete()
        return redirect('/')

    context = {'delete_store': store}
    return render(request, 'movie/deleteStore.html', context)


def addActor(request):
    form = ActorForm()
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'movie/addActor.html', context)


def updateActor(request, pk_actor):
    actor = Actor.objects.get(id=pk_actor)
    form = ActorForm(instance=actor)

    if request.method == 'POST':
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'movie/addActor.html', context)


def deleteActor(request, pk_actor):
    actor = Actor.objects.get(id=pk_actor)

    if request.method == "POST":
        actor.delete()
        return redirect('/')

    context = {'delete_actor': actor}
    return render(request, 'movie/deleteActor.html', context)


def addDirector(request):
    form = DirectorForm()
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'movie/addDirector.html', context)


def updateDirector(request, pk_director):
    director = Director.objects.get(id=pk_director)
    form = DirectorForm(instance=director)

    if request.method == 'POST':
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'movie/addDirector.html', context)


def deleteDirector(request, pk_director):
    director = Director.objects.get(id=pk_director)

    if request.method == "POST":
        director.delete()
        return redirect('/')

    context = {'delete_director': director}
    return render(request, 'movie/deleteDirector.html', context)