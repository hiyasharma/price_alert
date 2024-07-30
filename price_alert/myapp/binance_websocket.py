import json
import threading
import websocket
from myapp.models import Alert
from myapp.serializers import AlertSerializer
# from utils.py import btc_price
from myapp.utils import btc_price
from django.contrib.auth.models import User,auth


def on_message(ws, message):
    data = json.loads(message)
    price = float(data['p'])
    btc_price['price'] = price
    queryset = Alert.objects.filter(status='CREATED')
    for qs in queryset:
        userDetails = User.objects.filter(username=qs.username)
        for ud in userDetails:
            if qs.currentPrice >= qs.amount and price<=qs.amount:
                send_email(price,ud.email)
                Alert.objects.filter(id=qs.id).update(status='TRIGGERED')
            if qs.currentPrice <= qs.amount and price>=qs.amount:
                send_email(price,ud.email)
                Alert.objects.filter(id=qs.id).update(status='TRIGGERED')

    

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("WebSocket connection opened.")

def start_websocket():
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/btcusdt@trade",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

def send_email(price,user):
    import smtplib
    from email.mime.text import MIMEText
    from decouple import config

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = config('EMAIL_HOST_USER')
    sender_password = config('EMAIL_HOST_PASSWORD')
    receiver_email = user

    subject = 'BTC Price Alert'
    body = f'The price of BTC has reached {price} USD.'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print('Email sent successfully')
    except Exception as e:
        print(f'Error sending email: {e}')

# Start the WebSocket client in a separate thread
websocket_thread = threading.Thread(target=start_websocket)
websocket_thread.daemon = True
websocket_thread.start()
