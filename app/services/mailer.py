import requests
from app.core.config import get_settings

settings = get_settings()


def send_email(to: str, subject: str, body: str, from_address: str | None = None):
    payload = {
        'to': to,
        'subject': subject,
        'body': body,
        'from': from_address or settings.mailer_from,
    }
    headers = {
        'Authorization': f'Bearer {settings.mailer_token}',
        'Content-Type': 'application/json',
    }
    try:
        requests.post(settings.mailer_url, json=payload, headers=headers, timeout=5)
    except Exception as exc:
        print(f'Error sending email: {exc}')
