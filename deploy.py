"""
Heroku/PythonAnywhere Deployment Guide
For trainee registration with backend processing
"""

# Add this to deploy to PythonAnywhere or Heroku

# Option 1: PythonAnywhere (Free tier available)
# 1. Sign up at pythonanywhere.com
# 2. Upload trainee_backend.py and trainee_form.html
# 3. Create Web App → Python Flask
# 4. Set environment variables in Web tab
# 5. Point form action to your URL

# Option 2: Render.com (Free tier available)
# 1. Push code to GitHub
# 2. Connect repo on Render
# 3. Add environment variables:
#    GMAIL_EMAIL=minjaruli36@gmail.com
#    GMAIL_APP_PASSWORD=your_app_password
# 4. Deploy!

# Option 3: Railway.app (Free tier available)
# Similar to Render, connect GitHub repo and deploy

print("""
DEPLOYMENT OPTIONS:
===================

1. GITHUB PAGES (Frontend only)
   - Use trainee_form_emailjs.html
   - Requires EmailJS setup
   - No backend needed
   - Free forever

2. PYTHONANYWHERE (Full backend)
   - Free tier: 1 app, limited resources
   - Easy setup
   - Supports Python + PostgreSQL
   
3. RENDER.COM (Full backend)
   - Free tier: 750 hours/month
   - Auto-deploy from GitHub
   - Supports env variables
   
4. RAILWAY.APP (Full backend)
   - Free tier: $5/month credit
   - Auto-deploy from GitHub
   - Easy setup

5. YOUR OWN VPS (Oracle Cloud)
   - Already have this!
   - Run: python trainee_backend.py
   - Use nginx as reverse proxy
   - Free SSL with Certbot
""")
