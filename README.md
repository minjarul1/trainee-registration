# Trainee Registration System with Gmail App Password

A complete trainee registration form system that:
1. Collects trainee information via HTML form
2. Generates PDF registration form
3. Sends confirmation email with PDF attachment using Gmail SMTP

## 🚀 Quick Start

### Step 1: Get Gmail App Password

**This is required for the email functionality to work:**

1. Go to https://myaccount.google.com/apppasswords
2. Enable 2-Factor Authentication if not already enabled
3. Click **Create app password**
4. Select app: **Mail**
5. Select device: **Other (Custom name)**
6. Enter: `Hermes Agent Trainee System`
7. Click **Create**
8. **Copy the 16-character password** (e.g., `abcd efgh ijkl mnop`)

### Step 2: Configure Environment

Create a `.env` file in the project root:

```bash
GMAIL_EMAIL=minjaruli36@gmail.com
GMAIL_APP_PASSWORD=your_16_character_app_password_here
```

Or set as environment variables:
```bash
export GMAIL_EMAIL="minjaruli36@gmail.com"
export GMAIL_APP_PASSWORD="your_16_character_app_password_here"
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the System

**Option A: Standalone Server (Recommended for testing)**
```bash
python trainee_backend.py
```

**Option B: Flask Web App (For deployment)**
```bash
python -c "from trainee_backend import create_flask_app; app = create_flask_app(); app.run(debug=True)"
```

Then open http://localhost:5000 in your browser.

## 📁 Repository Structure

```
trainee-registration/
├── trainee_form.html          # Frontend form (works standalone)
├── trainee_form_emailjs.html  # Alternative with EmailJS (no backend)
├── trainee_backend.py         # Backend with PDF generation + email
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── .github/workflows/
    └── deploy.yml             # GitHub Pages auto-deploy
```

## 🔧 How It Works

### Flow:
```
User fills form → Submit → Backend receives data
                          ↓
              Generate PDF with trainee info
                          ↓
              Send email via Gmail SMTP
                          ↓
              User receives confirmation + PDF
```

### Key Components:

1. **HTML Form** (`trainee_form.html`)
   - Beautiful, responsive design
   - Bengali (Bangla) support
   - File upload for photo & signature
   - Form validation

2. **Backend Processing** (`trainee_backend.py`)
   - PDF generation using ReportLab
   - Gmail SMTP email sending
   - App Password authentication
   - Error handling & logging

3. **Email Template**
   - Professional HTML email
   - PDF attachment included
   - Mobile-responsive design

## 📧 Gmail SMTP Configuration

The system uses Gmail's SMTP server with App Password authentication:

| Setting | Value |
|---------|-------|
| SMTP Host | `smtp.gmail.com` |
| SMTP Port | `587` (TLS) or `465` (SSL) |
| Authentication | App Password (not regular password) |
| Daily Limit | 500 recipients per day (free) |

## 🔒 Security Notes

- ⚠️ **NEVER commit your App Password to Git**
- Use environment variables or `.env` file
- The `.env` file is in `.gitignore`
- App Passwords can be revoked anytime from Google Account settings
- Regular Gmail passwords don't work with SMTP - you MUST use App Passwords

## 🌐 Deployment Options

### Option 1: GitHub Pages (Frontend Only)
Use `trainee_form_emailjs.html` with EmailJS for email sending without backend.

### Option 2: PythonAnywhere (Full Backend - Free)
1. Sign up at pythonanywhere.com
2. Upload all files
3. Configure Flask web app
4. Set environment variables in dashboard

### Option 3: Render.com (Free Tier)
1. Push code to GitHub (already done)
2. Connect repo on Render
3. Add environment variables
4. Deploy automatically

### Option 4: Your Oracle Cloud VPS (Current)
```bash
# On your Oracle Cloud instance
cd /home/ubuntu/.hermes/downloads/TRAINEE_SYSTEM
python trainee_backend.py
# Access at http://your-server-ip:5000
```

## 🧪 Testing

Run the test script to verify everything works:

```bash
python trainee_backend.py
```

This will:
1. Generate a sample PDF
2. Try to send a test email (will fail if app password not set)
3. Show status messages

## 📝 Form Fields

The registration form collects:
- Personal Info (Name EN/BN, DOB, NID, Email, Phone)
- Address (Permanent + Present)
- Family Profile (Parents, Occupation, Income)
- Education (Degree, Institute, Year, Grade)
- Employment Status
- Documents (Photo, Signature)

## 🎨 Customization

### Change Email Template
Edit the HTML in `send_confirmation_email()` function in `trainee_backend.py`

### Change PDF Layout
Edit the `generate_trainee_pdf()` function using ReportLab styles

### Add More Fields
Add fields to both the HTML form and the backend processing

## 🐛 Troubleshooting

### "Authentication failed" Error
- Check your App Password is correct (16 characters, no spaces)
- Ensure 2FA is enabled on Google Account
- Verify you're using an App Password, not your regular Gmail password

### Email Not Sending
- Check spam folder
- Verify you haven't exceeded daily limit (500/day)
- Check Gmail security settings allow less secure apps (though App Password should bypass this)

### PDF Generation Fails
- Ensure ReportLab is installed: `pip install reportlab`
- Check file permissions
- Verify input data is not None

## 📚 Resources

- [Gmail App Passwords Guide](https://support.google.com/accounts/answer/185833)
- [ReportLab Documentation](https://www.reportlab.com/docs/reportlab-userguide.pdf)
- [SMTPLib Python Docs](https://docs.python.org/3/library/smtplib.html)

## 🤝 Contributing

Feel free to fork and improve! Just remember to keep your credentials secure.

## 📄 License

MIT License - Free to use for personal and commercial projects.

---

**Need help?** Create an issue on GitHub or contact the developer.
