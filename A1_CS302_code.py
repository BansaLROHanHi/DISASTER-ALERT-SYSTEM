import os
import smtplib
from email.mime.text import MIMEText
users = {
    "user1": {"location": "Sunder Nagar", "email": "b22111@students.iitmandi.ac.in"},
    "user2": {"location": "Mandi", "email": "user2@example.com"},
    "user3": {"location": "Kullu", "email": "b22134@students.iitmandi.ac.in"}
}

def validate_location(location):
    """Validates if the specified location exists in the user database."""
    valid_locations = {details["location"] for details in users.values()}
    return location in valid_locations

def send_email(email, subject, body):
    """Sends an email alert to the specified recipient."""
    sender_email = "sample@gmail.com"  # Replace with your Gmail address
    app_password = "sample password [16 letters]"  # Replace with your actual app password

    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = email

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
        print(f"Email sent to {email}")

    except Exception as e:
        print(f"Failed to send email to {email}: {e}")

def send_alert(location, message):
    """Sends alerts to users in the specified location."""
    if not validate_location(location):
        print(f"Error: '{location}' is not a valid location.")
        return

    print(f"\nSending Alert for {location}: {message}")
    recipients = [details["email"] for details in users.values() if details["location"] == location]

    if recipients:
        for email in recipients:
            send_email(email, f"Disaster Alert: {location}", message)
    else:
        print("No users found in this location.")

if __name__ == "_main_":
    print("=== Disaster Alert System ===")
    location = input("Enter affected location: ").strip()
    message = input("Enter alert message: ").strip()
    send_alert(location, message)
