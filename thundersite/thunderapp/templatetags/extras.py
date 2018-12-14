from django import template
from datetime import datetime

def display_message(message):
    time = str(message.time)[:16] + ' '
    # time = pretty_date(message.time)+ ' '
    heading ='<div class="media chat-item">'
    img= '<img alt="William" src="'+message.sender.profileImage.url+'" class="rounded-circle user-avatar-lg">'
    headerTitle = ' <div class="media-body"><div class="chat-item-title"><span class="chat-item-author">'+message.sender.username+'</span>'
    timetext = '<span>'+time+'</span></div>'
    text = '<div class="chat-item-body"><p>'+message.text + '</p></div></div>'
    return  heading + img +   headerTitle+ timetext + text + '</div>'

def display_all_messages(messages):
    messageString =""
    if len(messages)>0:
        for message in messages:
            messageString +=display_message(message)
        return messageString
    else:
        return "<br><span class='info'>No messages yet...😉 Type a message to your new match</span><br><br>"

def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time,datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff / 60) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(second_diff / 3600) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        return str(day_diff / 7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff / 30) + " months ago"
    return str(day_diff / 365) + " years ago"

register = template.Library()
register.filter('display_message', display_message)
register.filter('display_all_messages', display_all_messages)