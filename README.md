# login-authentication
front page for the application


###################
# Install dependencies
pip install twilio requests django

# Run the standalone logic demo
python otp_logic.py

# Run the full Django project
cd booking_auth
python manage.py migrate
python manage.py runserver
# Open: http://localhost:8000/login/
