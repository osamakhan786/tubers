from django.shortcuts import redirect, render
from .models import Tubercontact
# Create your views here.
from django.contrib import messages


   
# Create your views here.
def tubercontacts(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        user_id = request.POST['user_id']
        company = request.POST['company']
        phone = request.POST['phone']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        

        # TODO: do all sanitization
        tubercontacts = Tubercontact(full_name=full_name, company=company, user_id=user_id,
                                    phone=phone, email=email, subject=subject, message=message)
        tubercontacts.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('contact')