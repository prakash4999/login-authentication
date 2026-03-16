# Simulated in-memory store — in Django this is your database
users_db = {}

def get_or_create_user(method: str, destination: str) -> dict:
    """
    Look up a user by email or phone.
    Creates a new account automatically on first login.
    """
    key = f"{method}:{destination}"

    if key not in users_db:
        # First time this person signs in — create an account
        user = {
            "id":          len(users_db) + 1,
            "method":      method,
            "destination": destination,
            "email":       destination if method == "email" else None,
            "phone":       destination if method == "phone" else None,
            "created_at":  datetime.now().isoformat(),
            "is_new":      True,
        }
        users_db[key] = user
        print(f"New user created: {destination}")
    else:
        users_db[key]["is_new"] = False

    return users_db[key]

# Example
user = get_or_create_user("email", "john@gmail.com")
print(user)
