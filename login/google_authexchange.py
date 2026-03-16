import requests
import urllib.parse

CLIENT_ID     = "your_client_id.apps.googleusercontent.com"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI  = "http://localhost:8000/auth/google/callback/"

def get_google_login_url() -> str:
    """Build the Google OAuth2 URL to redirect users to."""
    params = {
        "client_id":     CLIENT_ID,
        "redirect_uri":  REDIRECT_URI,
        "response_type": "code",
        "scope":         "openid email profile",
        "access_type":   "offline",
        "prompt":        "select_account",
    }
    return "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode(params)


def get_google_user_info(auth_code: str) -> dict | None:
    """
    Exchange the auth code from Google for user profile info.
    Returns dict with email, name, picture, google_id — or None on failure.
    """
    # Step 1: exchange code for access token
    token_res = requests.post("https://oauth2.googleapis.com/token", data={
        "code":          auth_code,
        "client_id":     CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri":  REDIRECT_URI,
        "grant_type":    "authorization_code",
    })

    if not token_res.ok:
        print("Token exchange failed:", token_res.text)
        return None

    access_token = token_res.json().get("access_token")

    # Step 2: fetch the user's profile
    profile_res = requests.get(
        "https://www.googleapis.com/oauth2/v3/userinfo",
        headers={"Authorization": f"Bearer {access_token}"}
    )

    if not profile_res.ok:
        print("Profile fetch failed:", profile_res.text)
        return None

    data = profile_res.json()
    return {
        "email":     data.get("email"),
        "name":      data.get("name", ""),
        "picture":   data.get("picture", ""),
        "google_id": data.get("sub"),   # unique Google user ID
    }
