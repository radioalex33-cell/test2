import os

# Debugging code to print environment variables
print("Debugging Environment Variables:")
print("EMAIL:", os.getenv('GARMIN_EMAIL'))  # Assuming 'GITHUB_EMAIL' is the name of the secret
print("PASSWORD:", os.getenv('GARMIN_PASSWORD'))  # Assuming 'GITHUB_PASSWORD' is the name of the secret

# Check if email and password are received
if os.getenv('GARMIN_EMAIL') is not None:
    print("Email is being received from GitHub secrets.")
else:
    print("Email is NOT being received from GitHub secrets.")

if os.getenv('GARMIN_PASSWORD') is not None:
    print("Password is being received from GitHub secrets.")
else:
    print("Password is NOT being received from GitHub secrets.")