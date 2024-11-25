import yagmail

def send_email(subject, body, to_email, sender_email, app_password):
    yag = yagmail.SMTP(sender_email, app_password)
    yag.send(
        to=to_email,
        subject=subject,
        contents=body
    )
