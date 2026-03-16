// For SMS OTP — call Twilio Verify or MSG91
async function sendPhoneOTP() {
  await fetch('/api/otp/send', {
    method: 'POST',
    body: JSON.stringify({ phone: countryCode + phoneNumber })
  });
}

// For Email OTP — call your backend (Resend + random 6-digit code)
async function sendEmailOTP() {
  await fetch('/api/otp/send-email', {
    method: 'POST',
    body: JSON.stringify({ email })
  });
}

// For Google — integrate Firebase Auth or NextAuth Google provider
