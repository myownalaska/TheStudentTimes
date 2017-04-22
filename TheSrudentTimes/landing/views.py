from django.shortcuts import render
from .form import SubscriberForm
def landing(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)

        new_form=form.save()

    return render(request,'landing/index.html', locals())