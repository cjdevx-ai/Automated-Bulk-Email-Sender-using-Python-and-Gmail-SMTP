# Automated Bulk Email Sender using Python and Gmail SMTP

A Python application that automates sending bulk emails using Gmail's SMTP server. This tool allows you to send personalized emails to multiple recipients from a CSV file.

## Features

- 📧 Send bulk emails to multiple recipients
- 📊 Load recipient emails from CSV file
- 🔒 Secure SSL/TLS connection
- ⏱️ Built-in delay between emails to prevent spam detection
- 📝 Customizable email subject and body
- 📋 Easy-to-use configuration

## Prerequisites

- Python 3.6 or higher
- Gmail account with App Password enabled
- CSV file with recipient email addresses

## Installation

1. Clone or download this repository
2. Setup Python

```bash
python --version
```

```bash
pip -m venv .venv
```

```bash
.venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Setup Instructions

### 1. Gmail App Password Setup

To use Gmail SMTP, you need to create an App Password:

1. Go to your [Google Account settings](https://myaccount.google.com/)
2. Navigate to **Security** → **2-Step Verification** (enable if not already)
3. Go to **App passwords** and generate a new app password
4. Select **Mail** as the app and **Other** as the device
5. Copy the generated 16-character password

📺 **Tutorial Reference**: For detailed setup instructions, watch this [YouTube tutorial](https://youtu.be/2D8jpws-4hA) on how to get Gmail App Password.

### 2. Configure Email Settings

Edit the `main.py` file and update the following variables:

```python
# Define email sender details
email_sender = 'your-email@gmail.com'        # Your Gmail address
email_password = 'your-app-password'          # Your 16-character app password
```

### 3. Prepare Email Content

Update the email subject and body in `main.py`:

```python
subject = 'Your Email Subject Here'

body = """
Your email body content here.
You can write multiple lines.
"""
```

### 4. Prepare Recipients CSV

Ensure your `emails.csv` file has the following structure:

```csv
email_add
recipient1@example.com
recipient2@example.com
recipient3@example.com
```

**Important**: The CSV file must have a column named `email_add` containing the recipient email addresses.

## Usage

1. Place your recipient emails in `emails.csv`
2. Configure your email settings in `main.py`
3. Run the application:

```bash
python main.py
```

The application will:
- Load email addresses from the CSV file
- Connect to Gmail SMTP server
- Send emails to each recipient with a 2-second delay between emails
- Display progress in the console

## File Structure

```
├── main.py              # Main application file
├── emails.csv           # CSV file with recipient emails
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Security Notes

- ⚠️ **Never commit your actual email credentials to version control**
- 🔐 Use App Passwords instead of your regular Gmail password
- 📧 Be mindful of Gmail's sending limits (500 emails per day for free accounts)
- 🚫 Respect anti-spam policies and recipient preferences

## Troubleshooting

### Common Issues

1. **Authentication Error**: 
   - Verify your App Password is correct
   - Ensure 2-Step Verification is enabled on your Gmail account

2. **CSV File Error**:
   - Check that your CSV has a column named `email_add`
   - Ensure email addresses are valid

3. **SMTP Connection Error**:
   - Check your internet connection
   - Verify Gmail SMTP settings (smtp.gmail.com:465)

### Gmail Sending Limits

- **Free Gmail**: 500 emails per day
- **Google Workspace**: 2000 emails per day
- **Rate limiting**: Gmail may temporarily block accounts that send too many emails too quickly

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This tool is for legitimate email marketing and communication purposes only. Users are responsible for complying with applicable laws and regulations, including CAN-SPAM Act and GDPR. Always obtain proper consent before sending bulk emails.
