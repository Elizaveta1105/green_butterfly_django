# 🦋 Green Butterfly

**Green Butterfly** is a web application for managing finances and monitoring the progress of large-scale offline projects such as home renovations or house construction. It combines financial tracking with visual documentation, helping users stay on top of both budgets and results.

🌐 [Live Project Link](http://env-greenbutterfly.eba-wm879vm3.us-east-1.elasticbeanstalk.com/)

Please, sign up or use test user: _elizaveta11 / konkordiya05_

---

## 🧰 Key Features

- 📊 **Financial Tracking**: Log and categorize expenses to get a clear picture of your project’s budget.
- 📸 **Progress Visualization**: Upload photos to document work stages or store receipts for purchases.
- 🗃️ **Project Organization**: Create sections and spending depending on the scale of project.
- 🔒 **Secure & Scalable**: Deployed on AWS with static assets stored in Amazon S3 for efficient delivery.

For now, only one project is possible.
Features to add in future:
- Roles to manage projects from several accounts.
- Possibility to add several projects.

---

## 🛠 Tech Stack

- **Backend & Frontend**: [Django](https://www.djangoproject.com/)
- **Deployment**: [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)
- **Static Files Hosting**: [Amazon S3](https://aws.amazon.com/s3/)
- **Storing uploaded images**: [Cloudinary](https://cloudinary.com/)
- **DB: PostgreSQL**

---

## 🚀 Getting Started (for local development)

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd green-butterfly

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver

Ensure your .env or configuration includes proper AWS credentials for access.