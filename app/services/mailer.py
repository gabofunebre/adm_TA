import requests
from app.core.config import get_settings

settings = get_settings()


def send_email(to: str, subject: str, body: str, from_address: str | None = None):
    payload = {
        'to': to,
        'subject': subject,
        'body': body,
        'from': from_address or settings.MAILER_FROM,
    }
    headers = {
        'Authorization': f'Bearer {settings.MAILER_TOKEN}',
        'Content-Type': 'application/json',
    }
    try:
        requests.post(settings.MAILER_URL, json=payload, headers=headers, timeout=5)
    except Exception as exc:
        print(f'Error sending email: {exc}')
