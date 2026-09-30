"""
Trainee Registration Backend
Handles form submission, PDF generation, and email sending with Gmail App Password
"""

import os
import json
import smtplib
import ssl
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ============================================================
# CONFIGURATION - Set these values
# ============================================================

# Gmail App Password (GET FROM: Google Account → Security → App Passwords)
GMAIL_EMAIL = os.getenv("GMAIL_EMAIL", "minjaruli36@gmail.com")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD", "")  # Set this!
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

# PDF Output Directory
OUTPUT_DIR = Path("/home/ubuntu/.hermes/downloads/trainee_pdfs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# PDF GENERATION
# ============================================================

def generate_trainee_pdf(form_data, trainee_name):
    """Generate PDF registration form for trainee."""
    
    filename = f"trainee_{trainee_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    filepath = OUTPUT_DIR / filename
    
    # Create PDF with ReportLab
    doc = SimpleDocTemplate(
        str(filepath),
        pagesize=A4,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        alignment=1,  # Center
        spaceAfter=20
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=12,
        spaceBefore=15,
        spaceAfter=10
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        leading=14
    )
    
    # Build PDF content
    story = []
    
    # Title
    story.append(Paragraph("Trainee Registration Form", title_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Personal Information
    story.append(Paragraph("Personal Information", heading_style))
    personal_data = [
        ['Field', 'Value'],
        ['Full Name (EN)', form_data.get('fullNameEn', 'N/A')],
        ['Full Name (BN)', form_data.get('fullNameBn', 'N/A') or 'N/A'],
        ['Date of Birth', form_data.get('dob', 'N/A')],
        ['National ID', form_data.get('nid', 'N/A')],
        ['Email', form_data.get('email', 'N/A')],
        ['Phone', form_data.get('phone', 'N/A')],
    ]
    personal_table = Table(personal_data, colWidths=[2.5*inch, 4.5*inch])
    personal_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f8f9fa')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    story.append(personal_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Address
    story.append(Paragraph("Address", heading_style))
    address_data = [
        ['Type', 'Address'],
        ['Permanent', form_data.get('permanentAddress', 'N/A')],
        ['Present', form_data.get('presentAddress', 'N/A')],
    ]
    address_table = Table(address_data, colWidths=[2*inch, 5*inch])
    address_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
    ]))
    story.append(address_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Family Profile
    story.append(Paragraph("Family Profile", heading_style))
    family_data = [
        ['Father\'s Name', form_data.get('fatherName', 'N/A')],
        ['Mother\'s Name', form_data.get('motherName', 'N/A')],
        ['Father\'s Occupation', form_data.get('fatherOccupation', 'N/A')],
        ['Annual Income', form_data.get('income', 'N/A')],
    ]
    family_table = Table([[k, v] for k, v in family_data], colWidths=[2.5*inch, 4.5*inch])
    family_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
    ]))
    story.append(family_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Education
    story.append(Paragraph("Education", heading_style))
    edu_data = [
        ['Highest Education', form_data.get('education', 'N/A')],
        ['Institute', form_data.get('institute', 'N/A')],
        ['Passing Year', form_data.get('passingYear', 'N/A')],
        ['Grade/GPA', form_data.get('grade', 'N/A')],
    ]
    edu_table = Table([[k, v] for k, v in edu_data], colWidths=[2.5*inch, 4.5*inch])
    edu_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
    ]))
    story.append(edu_table)
    
    # Footer
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph(
        f"<i>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</i>",
        ParagraphStyle('Footer', fontSize=8, alignment=1)
    ))
    
    # Build PDF
    doc.build(story)
    
    return filepath


# ============================================================
# EMAIL SENDING
# ============================================================

def send_confirmation_email(trainee_email, trainee_name, pdf_path):
    """Send confirmation email with PDF attachment via Gmail SMTP."""
    
    if not GMAIL_APP_PASSWORD:
        return {
            "success": False,
            "message": "Gmail App Password not configured. Set GMAIL_APP_PASSWORD environment variable."
        }
    
    subject = f"Trainee Registration Confirmed - {trainee_name}"
    
    # HTML Email Body
    body_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }}
            .content {{ padding: 30px; background: #f9f9f9; }}
            .details {{ background: white; padding: 20px; border-radius: 5px; margin: 20px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            .footer {{ text-align: center; padding: 20px; color: #666; font-size: 12px; border-top: 1px solid #ddd; margin-top: 20px; }}
            h1 {{ margin: 0; font-size: 24px; }}
            h2 {{ color: #2c3e50; margin-top: 0; }}
            .btn {{ display: inline-block; padding: 12px 30px; background: #667eea; color: white; text-decoration: none; border-radius: 5px; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>✅ Registration Confirmed</h1>
        </div>
        <div class="content">
            <p>Dear <strong>{trainee_name}</strong>,</p>
            <p>Thank you for registering! Your application has been received successfully.</p>
            
            <div class="details">
                <h2>Your Registration Details</h2>
                <p><strong>Name:</strong> {trainee_name}</p>
                <p><strong>Email:</strong> {trainee_email}</p>
                <p><strong>Registration Date:</strong> {datetime.now().strftime('%B %d, %Y')}</p>
            </div>
            
            <p>Please find your registration form attached as PDF for your records.</p>
            <p>We will review your application and contact you within 3-5 business days.</p>
            
            <a href="#" class="btn">View Application Status</a>
        </div>
        <div class="footer">
            <p>This is an automated message. Please do not reply to this email.</p>
            <p>© 2026 Trainee Registration System</p>
        </div>
    </body>
    </html>
    """
    
    # Create message
    msg = MIMEMultipart("alternative")
    msg["From"] = GMAIL_EMAIL
    msg["To"] = trainee_email
    msg["Subject"] = subject
    
    # Attach HTML
    msg.attach(MIMEText(body_html, "html", "utf-8"))
    
    # Attach PDF
    if Path(pdf_path).exists():
        with open(pdf_path, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {Path(pdf_path).name}",
        )
        msg.attach(part)
    
    try:
        # Send via Gmail SMTP
        context = ssl.create_default_context()
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls(context=context)
        server.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_EMAIL, [trainee_email], msg.as_string())
        server.quit()
        
        return {
            "success": True,
            "message": f"Email sent to {trainee_email}"
        }
    except smtplib.SMTPAuthenticationError:
        return {
            "success": False,
            "message": "Authentication failed. Check GMAIL_APP_PASSWORD."
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Email error: {e}"
        }


# ============================================================
# MAIN PROCESSING
# ============================================================

def process_trainee_form(form_data):
    """Process form submission: generate PDF and send email."""
    
    # Extract trainee info
    trainee_name = form_data.get('fullNameEn', 'Unknown')
    trainee_email = form_data.get('email', '')
    
    if not trainee_email:
        return {"success": False, "message": "Email is required"}
    
    # Generate PDF
    pdf_path = generate_trainee_pdf(form_data, trainee_name)
    print(f"📄 PDF generated: {pdf_path}")
    
    # Send email
    email_result = send_confirmation_email(trainee_email, trainee_name, pdf_path)
    
    if email_result['success']:
        return {
            "success": True,
            "message": "Registration completed successfully!",
            "pdf_path": str(pdf_path),
            "email_status": email_result['message']
        }
    else:
        return {
            "success": False,
            "message": f"PDF generated but email failed: {email_result['message']}",
            "pdf_path": str(pdf_path)
        }


# ============================================================
# FLASK API (for GitHub Pages deployment)
# ============================================================

def create_flask_app():
    """Create Flask app for web deployment."""
    from flask import Flask, request, jsonify
    from flask_cors import CORS
    
    app = Flask(__name__)
    CORS(app)
    
    @app.route('/api/submit', methods=['POST'])
    def submit_form():
        data = request.json
        result = process_trainee_form(data)
        return jsonify(result)
    
    @app.route('/')
    def index():
        return """
        <h1>Trainee Registration System</h1>
        <p>Use the HTML form to submit registration.</p>
        """
    
    return app


if __name__ == "__main__":
    print("=" * 50)
    print("Trainee Registration System")
    print("=" * 50)
    print(f"\nGmail: {GMAIL_EMAIL}")
    print(f"Output Dir: {OUTPUT_DIR}")
    
    if not GMAIL_APP_PASSWORD:
        print("\n⚠️ WARNING: GMAIL_APP_PASSWORD not set!")
        print("Set it using: export GMAIL_APP_PASSWORD='your_app_password'")
        print("\nTo get app password:")
        print("1. Go to: https://myaccount.google.com/apppasswords")
        print("2. Enable 2FA if not already enabled")
        print("3. Create app password for 'Mail'")
        print("4. Copy the 16-character password")
    else:
        print("\n✓ Gmail App Password configured")
        
        # Test with sample data
        test_data = {
            'fullNameEn': 'Test User',
            'fullNameBn': 'টেস্ট ইউজার',
            'dob': '1995-01-15',
            'nid': '1234567890123',
            'email': 'test@example.com',
            'phone': '+880 1711-104318',
            'permanentAddress': 'Test Village, Test District',
            'presentAddress': 'Test Address, Test City',
            'fatherName': 'Test Father',
            'motherName': 'Test Mother',
            'fatherOccupation': 'Business',
            'income': '300k_500k',
            'education': 'bachelors',
            'institute': 'Test University',
            'passingYear': '2020',
            'grade': '3.75',
            'employmentStatus': 'student',
            'monthlyIncome': '',
        }
        
        print("\n🧪 Testing with sample data...")
        result = process_trainee_form(test_data)
        print(f"Result: {result}")
