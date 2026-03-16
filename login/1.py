import random
import string
from datetime import datetime, timedelta

def generate_otp(length=6):
    """Generate a random numeric OTP."""
    return ''.join(random.choices(string.digits, k=length))

def get_expiry(minutes=10):
    """Return expiry datetime from now."""
    return datetime.now() + timedelta(minutes=minutes)

# Example
otp = generate_otp()
expires = get_expiry()
print(f"OTP: {otp}, Expires at: {expires}")
