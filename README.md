# Trainee Registration System

A complete trainee registration form with automatic PDF generation and email confirmation.

## Features

- ✅ Modern responsive HTML form
- ✅ Automatic PDF generation with trainee data
- ✅ Email confirmation with PDF attachment
- ✅ Gmail SMTP integration with App Password
- ✅ Bengali (Bangla) support
- ✅ File upload for photo & signature
- ✅ GitHub Pages compatible

## Setup

### 1. Get Gmail App Password

1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Enable **2-Step Verification** (if not already enabled)
3. Go to [App Passwords](https://myaccount.google.com/apppasswords)
4. Create app password for "Mail" → Name it "Hermes Agent"
5. Copy the 16-character password

### 2. Configure Environment

```bash
# Set your Gmail credentials
export GMAIL_EMAIL="minjaruli36@gmail.com"
export GMAIL_APP_PASSWORD="abcd efgh ijkl mnop"  # Your app password

# Or create .env file
echo 'GMAIL_EMAIL=minjaruli36@gmail.com' > .env
echo 'GMAIL_APP_PASSWORD=your_app_password_here' >> .env
```

### 3. Install Dependencies

```bash
pip install reportlab flask flask-cors
```

### 4. Run the Backend

```bash
python trainee_backend.py
```

### 5. Deploy to GitHub Pages

1. Create a new GitHub repository
2. Upload these files:
   - `trainee_form.html`
   - `trainee_backend.py`
   - `requirements.txt`
   - `README.md`

3. Enable GitHub Pages:
   - Settings → Pages → Source: main branch
   - Deploy from folder: `/`

## Usage

### Using the HTML Form

Open `trainee_form.html` in a browser and fill out the form. On submission:

1. PDF is generated with all trainee information
2. Confirmation email is sent to the trainee with PDF attached
3. Success/error message is displayed

### Using the Backend API

```python
from trainee_backend import process_trainee_form

result = process_trainee_form({
    'fullNameEn': 'John Doe',
    'email': 'john@example.com',
    # ... other fields
})

print(result)
# {'success': True, 'message': 'Registration completed successfully!', ...}
```

## Form Fields

| Section | Fields |
|---------|--------|
| Personal | Full Name (EN/BN), DOB, NID, Email, Phone |
| Address | Permanent Address, Present Address |
| Family | Father/Mother Name, Occupation, Income |
| Education | Highest Education, Institute, Year, Grade |
| Employment | Status, Monthly Income |
| Documents | Passport Photo, Signature |

## GitHub Repository Structure

```
trainee-registration/
├── trainee_form.html      # Frontend form
├── trainee_backend.py     # Backend processing
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── .github/
    └── workflows/
        └── deploy.yml     # Auto-deploy to GitHub Pages
```

## Security Notes

- ⚠️ **Never commit your Gmail App Password to Git**
- Use environment variables or `.env` file
- The `.env` file should be in `.gitignore`
- App Passwords are preferred over regular passwords

## Troubleshooting

### Email not sending?
- Check GMAIL_APP_PASSWORD is correct
- Ensure 2FA is enabled on Google Account
- Check spam folder for delivery issues

### PDF looks wrong?
- ReportLab uses standard fonts by default
- For Bengali text, download FreeSans.ttf and register it

### GitHub Pages error?
- HTML form works standalone on GitHub Pages
- Backend requires a server (PythonAnywhere, Render, or VPS)
- Use Formspree.io as alternative for form submissions

## Alternative: Using Formspree

If you don't want to run a backend:

1. Sign up at https://formspree.io
2. Create a form and get your endpoint URL
3. Update the HTML form's `action` attribute:

```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST" enctype="multipart/form-data">
```

## License

MIT License - Feel free to use for your projects.
