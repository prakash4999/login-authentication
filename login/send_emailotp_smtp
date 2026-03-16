import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_otp(to_email: str, otp: str) -> tuple[bool, str]:
    """Send OTP via Gmail SMTP."""
    FROM_EMAIL = "your@gmail.com"
    APP_PASSWORD = "your_16char_app_password"  # Gmail App Password

    subject = f"Your sign-in code: {otp}"

    plain = f"Your one-time sign-in code is: {otp}\nExpires in 10 minutes."

    html = f"""
    <div style="font-family:sans-serif; max-width:480px; margin:0 auto; padding:32px;">
      <h2 style="color:#0d0d12;">Your sign-in code</h2>
      <p style="color:#7a7a90;">Valid for 10 minutes.</p>
      <div style="background:#f7f6f2; border-radius:12px; padding:24px;
                  text-align:center; letter-spacing:10px;
                  font-size:36px; font-weight:700; color:#0d0d12;">
        {otp}
      </div>
      <p style="color:#7a7a90; font-size:12px; margin-top:24px;">
        If you didn't request this, ignore this email.
      </p>
    </div>
    """

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = FROM_EMAIL
    msg["To"]      = to_email
    msg.attach(MIMEText(plain, "plain"))
    msg.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(FROM_EMAIL, APP_PASSWORD)
            server.sendmail(FROM_EMAIL, to_email, msg.as_string())
        return True, "Email sent successfully"
    except smtplib.SMTPAuthenticationError:
        return False, "Email auth failed. Check your Gmail App Password."
    except Exception as e:
        return False, f"Email failed: {str(e)}"

# Example
# success, msg = send_email_otp("user@gmail.com", "482916")
