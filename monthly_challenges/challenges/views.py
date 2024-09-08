from urllib import response
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
monthly_goals = {
    "January": "Start a fitness routine and stick to it for 4 weeks.",
    "February": "Read two new books on personal development.",
    "March": "Organize your workspace and declutter your home.",
    "April": "Start a new hobby or learn a new skill.",
    "May": "Plant a small garden or start an indoor plant collection.",
    "June": "Go on a weekend trip to explore a new city or town.",
    "July": "Challenge yourself to a week of daily meditation.",
    "August": "Volunteer for a local charity or community event.",
    "September": "Complete an online course to improve your career skills.",
    "October": "Try cooking a new healthy recipe each week.",
    "November": "Set aside time for daily journaling and reflection.",
    "December": "Create a budget and savings plan for the next year."
}


def index(request):

    months_list = list(monthly_goals.keys())
    return render(request, "challenges/index.html", {
        "months": months_list
    })


def Number_monthly_challenges(request, month):
    months = list(monthly_goals.keys())
    redirect_month = months[month-1]
    # the reverse function in used to construct path by its given name
    redirect_path = reverse("month-challenge", args=[redirect_month])
    if (month > len(months)):
        return HttpResponseNotFound("invalid month ")
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        monthChallenge = monthly_goals[month]
        return render(request, "challenges/challenge.html", {
            "challenge_text": monthChallenge,
            "month_name": month
        })
    except:
        return HttpResponseNotFound("not supported Month")
