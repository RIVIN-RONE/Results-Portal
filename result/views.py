from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def login(request):
    if request.method == 'POST':
        rollnumber = request.POST['Rollnumber']
        DOB = request.POST['DOB']  # Change 'Name' to 'DOB'

        try:
            user = User.objects.get(Rollnumber=rollnumber, DOB=DOB)  # Change 'Name' to 'DOB'
            # User authentication successful, redirect to success page
            return redirect('success', rollnumber=rollnumber)
        except User.DoesNotExist:
            messages.error(request, 'Invalid DOB or Rollnumber!')  # Change 'Name' to 'DOB'

    return render(request, 'login.html')

def success(request, rollnumber):
    try:
        user = User.objects.get(Rollnumber=rollnumber)
        return render(request, 'success.html', {'user': user})
    except User.DoesNotExist:
        error_message = 'User not found.'
        return render(request, 'login.html', {'error_message': error_message})
