from datetime import datetime

def verify_otp(stored_otp, stored_expiry, stored_attempts, entered_otp, max_attempts=5):
    """
    Verify an entered OTP against the stored one.
    Returns (success: bool, message: str)
    """
    if stored_attempts >= max_attempts:
        return False, "Too many attempts. Request a new OTP."

    if datetime.now() > stored_expiry:
        return False, "OTP has expired. Please request a new one."

    if stored_otp != entered_otp.strip():
        remaining = max_attempts - (stored_attempts + 1)
        return False, f"Wrong OTP. {remaining} attempt(s) left."

    return True, "OTP verified successfully!"

# Example usage
stored = {
    "otp": "482916",
    "expires": datetime.now() + timedelta(minutes=10),
    "attempts": 0
}

success, msg = verify_otp(
    stored["otp"], stored["expires"],
    stored["attempts"], "482916"
)
print(success, msg)  # True  OTP verified successfully!
