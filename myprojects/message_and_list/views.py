from django.shortcuts import render, redirect
from django.contrib import messages

import hashlib


def check_my_password(password, my_password):
    ''' Compare input password with my password '''
    temp = hashlib.sha256()
    temp.update(password.encode('utf-8'))
    return temp.hexdigest() == my_password


def home(request):
    word_list = ['password', 'stupid', 'god']
    my_password = '10e357984b5596626dd74ea4b40bc2d6fc685174d735d35dd90a5c36ae21c415'

    if request.method == 'POST':
        check_password = request.POST['password']
        check_email = request.POST['email']
        
        # Check password is small or in word_list
        if check_password in word_list:
            messages.error(request, 'Password is so stupid')
            return redirect('index')
        if len(check_password) <= 4:
            messages.error(request, 'password is too short')

        if check_my_password(check_password, my_password):
            request.session['email'] = check_email
            return redirect('next_page')

    return render(request, 'message_and_list/index.html')


def next_page(request):
    email = request.session.get('email', 'Няма въведен')
    return render(request, 'message_and_list/show_message.html', {'email': email})
