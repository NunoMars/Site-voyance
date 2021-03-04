from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from .models import CustomUser
from clairvoyance.models import MajorArcana



def send_welcome_email(user):
    plaintext = get_template('accounts/email_account_created.txt')
    htmly     = get_template('accounts/email_account_created.html')

    context = { 'username': user.first_name }

    if user.user_language == 'en':
        sentence = 'Benvenu a mon site de voyance gratuit !!! '

    if user.user_language == 'es':
        sentence = 'Benvenu a mon site de voyance gratuit !!! '

    if user.user_language == 'pt':
        sentence = 'Benvindo ao meu site de cartonância gratuito!!'
    else:
        sentence = 'Benvenu a mon site de voyance gratuit !!! '

    subject, from_email, to = sentence, 'patricia.nunes.tarot@gmail.com', user.email
    text_content = plaintext.render(context)
    html_content = htmly.render(context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_one_card_daily_email():
    users = CustomUser.objects.all()

    for user in users:
        card = MajorArcana.objects.order_by('?')
        if user.user_language == 'pt':
            pass
        if user.user_language == 'en':
            pass
        if user.user_language == 'es':
            pass
        else:
            pass