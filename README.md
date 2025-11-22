# My Profile Web App

A Flask-based web application to showcase your professional profile and resume.

## Features

- **Profile Tab**: Displays contact information, skills, experience, education, and social links
- **Resume Tab**: Shows your PDF resume with download option
- **Responsive Design**: Works on desktop and mobile devices
- **Modern UI**: Clean and professional interface with gradient colors

## Setup

1. Install dependencies:
```bash
pip install flask
```

2. Run the application:
```bash
cd src
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

## Customization

Edit the `profile_data` dictionary in `src/app.py` to update your personal information:
- Name, title, email, phone, location
- Skills, experience, education
- Social media links

## Project Structure

```
myprofile/
├── docs/
│   └── RESUME_PRAKASH V.pdf
├── src/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
└── README.md
```
