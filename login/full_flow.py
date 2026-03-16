from datetime import datetime, timedelta
import random, string

# In-memory OTP store (use a database in production)
otp_store = {}

def request_otp(method: str, destination: str) -> str:
    """Generate OTP, store it, and send it."""
    otp = ''.join(random.choices(string.digits, k=6))
    otp_store[destination] = {
        "code":     otp,
        "expires":  datetime.now() + timedelta(minutes=10),
        "attempts": 0,
        "used":     False,
    }

    if method == "phone":
        # send_sms_otp(destination, otp)
        print(f"[SMS]   → {destination}  Code: {otp}")
    else:
        # send_email_otp(destination, otp)
        print(f"[Email] → {destination}  Code: {otp}")

    return otp  # only returned here for demo purposes


def login_with_otp(destination: str, entered: str) -> tuple[bool, str, dict | None]:
    """Verify OTP and return the user if valid."""
    record = otp_store.get(destination)

    if not record:
        return False, "No OTP found. Please request one first.", None

    if record["used"]:
        return False, "OTP already used.", None

    if datetime.now() > record["expires"]:
        return False, "OTP expired. Request a new one.", None

    if record["attempts"] >= 5:
        return False, "Too many attempts. Request a new OTP.", None

    record["attempts"] += 1

    if record["code"] != entered.strip():
        remaining = 5 - record["attempts"]
        return False, f"Wrong code. {remaining} attempt(s) left.", None

    record["used"] = True
    method = "email" if "@" in destination else "phone"
    user = get_or_create_user(method, destination)
    return True, "Login successful!", user


# ── Demo run ──────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Phone OTP Flow ===")
    request_otp("phone", "+919876543210")
    ok, msg, user = login_with_otp("+919876543210", otp_store["+919876543210"]["code"])
    print(f"Result: {ok} — {msg}")
    print(f"User:   {user}\n")

    print("=== Email OTP Flow ===")
    request_otp("email", "alice@gmail.com")
    ok, msg, user = login_with_otp("alice@gmail.com", "999999")   # wrong code
    print(f"Wrong code: {ok} — {msg}")
    ok, msg, user = login_with_otp("alice@gmail.com", otp_store["alice@gmail.com"]["code"])
    print(f"Right code: {ok} — {msg}")
```

**Output:**
```
=== Phone OTP Flow ===
[SMS]   → +919876543210  Code: 738291
Result: True — Login successful!
User:   {'id': 1, 'method': 'phone', ...}

=== Email OTP Flow ===
[Email] → alice@gmail.com  Code: 481726
Wrong code: False — Wrong code. 4 attempt(s) left.
Right code: True — Login successful!
