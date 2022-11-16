from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in,sender = User)
def loginsuccess(sender, request, user, **kwargs):
    print('logged_in signal....')
    ip = request.META.get('REMOTE_ADDR')
    print('user ip address is ',ip)
    request.session['ip'] = ip
