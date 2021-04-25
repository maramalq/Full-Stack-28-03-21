from django.shortcuts import render, redirect
from .models import Celebrity
from django.contrib import messages
from datetime import date
# Create your views here.


def index(request):
    if 'name' in request.session:
        return redirect("/celebrities")
    return render(request, "login.html")

    # return redirect("/celebrities")


def celebrities(request):
    if 'name' not in request.session:
        return redirect("/")
    context = {
        "all_celebrities": Celebrity.objects.all(),
        "user_name": request.session['name']
    }
    return render(request, "celebrities.html", context)


def celebrities_create(request):
    context = {
        'today': date.today()
    }
    return render(request, "new_celebrity.html", context)


def celebrity_show(request, celebrity_id):
    context = {
        "celebrity": Celebrity.objects.get(id=celebrity_id)
    }
    return render(request, "show_celebrity.html", context)


def celebrities_edit(request, celebrity_id):
    context = {
        "celebrity": Celebrity.objects.get(id=celebrity_id)
    }
    return render(request, "edit_celebrity.html", context)


def login(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['email'] = request.POST['email']
    return redirect("/celebrities")


def celebrities_new(request):
    # if request.method == "GET":
    #     return render()
    if request.method == "POST":
        # call the basic validator method from the CelebrityManager
        errors = Celebrity.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/celebrities/create")
        Celebrity.objects.create(
            name=request.POST['name'],
            image=request.POST['image'],
            occupation=request.POST['job'],
            debut_date=request.POST['debut']
        )
        print("creation successful")
    return redirect("/celebrities")


def celebrities_update(request, celebrity_id):
    if request.method == "POST":
        errors = Celebrity.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/celebrities/create")
        this_celebrity = Celebrity.objects.get(id=celebrity_id)
        this_celebrity.name = request.POST['name']
        this_celebrity.image = request.POST['image']
        this_celebrity.occupation = request.POST['job']
        this_celebrity.debut_date = request.POST['debut']
        this_celebrity.save()
    return redirect(f"/celebrities/{celebrity_id}")


def celebrities_destroy(request, celebrity_id):
    # if request.method == "POST":
    this_celebrity = Celebrity.objects.get(id=celebrity_id)
    this_celebrity.delete()
    return redirect("/celebrities")


def logout(request):
    request.session.flush()
    return redirect("/")
