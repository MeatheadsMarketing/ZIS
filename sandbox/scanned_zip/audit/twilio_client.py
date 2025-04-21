def send_sms():
    import os
    return f'Twilio SID: {os.getenv("TWILIO_ACCOUNT_SID")}'