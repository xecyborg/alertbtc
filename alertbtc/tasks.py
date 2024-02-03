from celery import shared_task
import requests
from django.core.mail import send_mail
from django.contrib.auth.models import User
from alerts.models import Alert

@shared_task
def fetch_price_and_send_emails():
    url = r'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    
    try:
        response = requests.get(url = url)
        response.raise_for_status()
        data = response.json()
        current_price = data[0]['current_price']

        users_to_notify = User.objects.filter(
            Q(target_price__lte=current_price) & Q(target_price__isnull=False)
        )

        for user in users_to_notify:
            try:
                send_mail(
                    subject='Target price reached!',
                    message=f'The price has reached your target of ${user.target_price}!',
                    from_email='dummy_mail@gmail.com',
                    recipient_list=[user.email],
                )
            except Exception as e:
                # Log the error and continue
                print(f"Error sending email to {user.email}: {e}")

    except Exception as e:
        print(f"Error fetching price or sending emails: {e}")
        raise fetch_price_and_send_emails.retry(exc=e)

    alerts = Alert.objects.all()

    for alert in alerts:
        if current_price <= alert.target_price:
            send_email_alert(alert.user.email, current_price, alert.target_price)

def send_email_alert(email, current_price, target_price):
    subject = 'Cryptocurrency Price Alert'
    message = f'The cryptocurrency price has reached your target price.\nCurrent Price: {current_price}\nTarget Price: {target_price}'
    from_email = 'your_email@gmail.com'

    send_mail(subject, message, from_email, [email])
