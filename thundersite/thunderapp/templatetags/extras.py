from django import template
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

def display_message(message, user, username):
    url = reverse('messages')
    time = str(message.time)[:16] + ' '
    # str(message.time.date()) + str(message.time.hour) + ':' + str(message.time.minute)
    sender = '<a href="' + url + '?view=' + message.sender.username + '">' + message.sender.username + '</a> '
    if message.public:
        text = 'wrote: ' + message.text + ' '
    else:
        text = 'whispered: <span class="whisper">' + message.text + '</span>' + ' '
    if message.sender.username==username or message.recip.username==username:
        button = '<button type="button" class="remove-btn">erase</button>'
    else:
        button = ''
    return '<div id="' + str(message.id) + '">' + time + sender + text + button + '</div>'

register = template.Library()
register.filter('display_message', display_message)