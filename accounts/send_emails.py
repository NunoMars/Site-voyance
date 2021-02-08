from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template



def send_welcome_email(user):
    plaintext = get_template('accounts/email_account_created.txt')
    htmly     = get_template('accounts/email_account_created.html')

    context = { 'username': user.first_name }

    subject, from_email, to = 'Benvindo/a ao mundo do Tarot !!! ', 'patricia.nunes.tarot@gmail.com', user.email
    text_content = plaintext.render(context)
    html_content = htmly.render(context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()