from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

# Profile data
profile_data = {
    'name': 'Prakash Vidjiacoumar',
    'title': 'DevOps Engineer',
    'email': 'prakashvidjiacoumar2002@gmail.com',
    'phone': '+91 6379396487',
    'location': 'India',
    'summary': 'DevOps Engineer with 3 years of experience specializing in infrastructure automation, MicroStrategy administration, and cloud solutions. Passionate about building efficient systems and automating workflows to enhance operational excellence.',
    'skills': [
        'Python', 'Terraform', 'Jenkins', 'MicroStrategy REST APIs',
        'PostgreSQL', 'Cloud (DoitNow)', 'Infrastructure Automation',
        'DevOps', 'CI/CD', 'Scripting', 'AI/ML', 'REST APIs'
    ],
    'experience': [
        {
            'title': 'DevOps Engineer (Full-Time)',
            'company': 'Societe Generale Global Solution Center',
            'period': 'July 2024 - Present',
            'description': 'Working in MicroStrategy Admin team, creating and maintaining infrastructure, installing and configuring MicroStrategy environments. Developing automation solutions using Python with MicroStrategy REST APIs and PostgreSQL databases. Configuring and managing CI/CD pipelines in Jenkins.'
        },
        {
            'title': 'DevOps Engineer Intern',
            'company': 'Societe Generale Global Solution Center',
            'period': 'February 2024 - June 2024 (4.5 months)',
            'description': 'Gained hands-on experience in infrastructure management, automation scripting, and MicroStrategy administration. Contributed to various automation projects and learned DevOps best practices.'
        }
    ],
    'projects': [
        {
            'name': 'Car Leasing Chatbot',
            'description': 'Developed an AI-powered chatbot for car leasing services using modern AI technologies, enhancing customer interaction and automating query responses.',
            'technologies': 'AI/ML, Python, Natural Language Processing'
        },
        {
            'name': 'Infrastructure Automation',
            'description': 'Created automated scripts and pipelines for infrastructure provisioning and MicroStrategy installations, reducing manual effort and deployment time significantly.',
            'technologies': 'Python, Terraform, Jenkins, MicroStrategy REST APIs'
        },
        {
            'name': 'Database Automation',
            'description': 'Developed automation solutions for PostgreSQL database management and maintenance tasks, integrated with MicroStrategy environments.',
            'technologies': 'Python, PostgreSQL, REST APIs'
        }
    ],
    'education': [
        {
            'degree': 'Bachelor of Technology',
            'institution': 'Sri Manakula Vinayagar Engineering College',
            'year': '2019 - 2023'
        }
    ],
    'social_links': {
        'github': 'https://github.com/Prakash-28',
        'linkedin': 'https://www.linkedin.com/in/prakash-v-117156193/'
    }
}

@app.route('/')
def home():
    return render_template('index.html', profile=profile_data)

@app.route('/resume')
def resume():
    # Try multiple possible locations
    base_dir = os.path.dirname(os.path.abspath(__file__))
    possible_paths = [
        os.path.join(base_dir, 'docs', 'RESUME_PRAKASH V.pdf'),
        os.path.join('/home/site/wwwroot', 'docs', 'RESUME_PRAKASH V.pdf'),
        os.path.join(base_dir, '..', 'docs', 'RESUME_PRAKASH V.pdf')
    ]
    
    for resume_path in possible_paths:
        if os.path.exists(resume_path):
            return send_file(resume_path, mimetype='application/pdf')
    
    # Debug info
    error_msg = f"Resume not found. Tried paths: {possible_paths}<br>"
    error_msg += f"Base dir: {base_dir}<br>"
    error_msg += f"Files in base: {os.listdir(base_dir) if os.path.exists(base_dir) else 'N/A'}<br>"
    docs_path = os.path.join(base_dir, 'docs')
    if os.path.exists(docs_path):
        error_msg += f"Files in docs: {os.listdir(docs_path)}"
    return error_msg, 404

if __name__ == '__main__':
    # Get port from environment variable (Azure assigns dynamic port)
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=False, host='0.0.0.0', port=port)
