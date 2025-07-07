# Calendar Integration Project

This project provides a Python-based interface for interacting with Google Calendar using a service account. It includes utilities for calendar management, access control, and a Streamlit web interface for user interaction.

## Features

- Google Calendar API integration using a service account
- Utilities for calendar operations (create, list, update, delete events)
- Access management
- Streamlit web app for easy interaction

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Yasvanth-2005/calender-booking
cd calender
```

### 2. Create and Activate a Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables Setup

**Important:**

- The project previously used a `credentials/service_account.json` file for Google API credentials. For better security and flexibility, you should now use environment variables.
- You can copy the example below into a `.env` file in the project root.

#### Example `.env` file

```
GOOGLE_TYPE=service_account
GOOGLE_PROJECT_ID=your-google-project-id
GOOGLE_PRIVATE_KEY_ID=your-private-key-id
GOOGLE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nMIIEv...\n-----END PRIVATE KEY-----\n"
GOOGLE_CLIENT_EMAIL=your-service-account-email@your-project.iam.gserviceaccount.com
GOOGLE_CLIENT_ID=your-client-id
GOOGLE_AUTH_URI=https://accounts.google.com/o/oauth2/auth
GOOGLE_TOKEN_URI=https://oauth2.googleapis.com/token
GOOGLE_AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
GOOGLE_CLIENT_X509_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/your-service-account-email@your-project.iam.gserviceaccount.com
GOOGLE_UNIVERSE_DOMAIN=googleapis.com
```

- Replace the values with your actual Google Cloud service account credentials.
- For the private key, keep the value in quotes and use `\n` for newlines.

#### Loading Environment Variables

The project uses the `python-dotenv` package to load environment variables from the `.env` file. Make sure to install it (it's included in `requirements.txt`).

---

## Credentials JSON

- The original `credentials/service_account.json` file contains sensitive information for Google API access.
- **Do not commit this file to version control.**
- For security, the project now uses environment variables instead of directly reading the JSON file.
- If you still have the JSON, you can convert its fields to environment variables as shown above.

---

## Running the Project

### 1. Streamlit Web App

To start the web interface:

```bash
streamlit run streamlit_app.py
```

### 2. Other Scripts

You can run other scripts (e.g., `main.py`, `grant_access.py`, etc.) as needed:

```bash
python main.py
```

---

## Requirements

- Python 3.7+
- See `requirements.txt` for all dependencies

---

## Security Notes

- **Never share your `.env` or credentials JSON file.**
- Always add `.env` and `credentials/service_account.json` to your `.gitignore`.
- Rotate your credentials if you suspect they have been exposed.

---

## Support

For issues or questions, please open an issue in the repository or contact the maintainer.
