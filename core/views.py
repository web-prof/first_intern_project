from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail

def main(request):
    return render(request, 'core/index.html', {})


def screen2(request):
    form = screen2_form(request.POST or None)
    if request.method == 'POST':
            if form.is_valid():
                first_name=form.cleaned_data['first_name']
                last_name=form.cleaned_data['last_name']
                email=form.cleaned_data['email']
                phone_number=form.cleaned_data['phone_number']
                operation_country=form.cleaned_data['operation_country']
                company_name=form.cleaned_data['company_name']
                objective=form.cleaned_data['objective']
                more_details=form.cleaned_data['more_details']
                subject=first_name+last_name+operation_country+company_name
                message=email+phone_number+objective+more_details
                send_mail(
                    subject,
                    message,
                    'ishakg24@gmail.com',
                    ['ishakg24@gmail.com'],
                )
            else:
                return redirect('core:screen3')
            return redirect('core:screen3')
    return render(request, 'core/screen2.html', {'form': form})


def screen3(request):
    return render(request, 'core/screen3.html', {})
