from twilio.rest import Client

def send_sms_otp(phone: str, otp: str) -> tuple[bool, str]:
    """Send OTP via Twilio SMS."""
    ACCOUNT_SID = "ACxxxxxxxxxxxxxxxx"
    AUTH_TOKEN  = "your_auth_token"
    FROM_PHONE  = "+1234567890"

    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        client.messages.create(
            body=f"Your verification code is: {otp}. Valid for 10 minutes.",
            from_=FROM_PHONE,
            to=phone
        )
        return True, "SMS sent successfully"
    except Exception as e:
        return False, f"SMS failed: {str(e)}"

# Example
# success, msg = send_sms_otp("+919876543210", "482916")
