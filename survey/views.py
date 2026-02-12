from django.shortcuts import render, redirect
from .forms import SurveyForm

def landing(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SurveyForm()

    return render(request, 'survey/landing.html', {'form': form})


def success(request):
    return render(request, 'survey/success.html')