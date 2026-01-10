# BlogSpot - Django Blogging Platform

A full-featured blogging application built with Django and Bootstrap. This platform allows users to share their stories, interact with other posts, and manage their own content.

## 🚀 Features

-   **User Authentication**: Secure Sign Up, Sign In, and Logout functionality.
-   **Create & Manage Posts**: Users can create rich blog posts with images and categories.
-   **Interactive Community**:
    -   **Likes**: Show appreciation for posts.
    -   **Comments**: Engage in discussions on blog posts.
-   **Profile Management**: Customize your user profile.
-   **Responsive Design**: Built with Bootstrap 5 for a seamless experience on mobile and desktop.
-   **Cloud Integration**: Media files are stored and served via Cloudinary.
-   **Contact Form**: Integrated contact mechanism.

## 🛠️ Tech Stack

-   **Backend**: [Django](https://www.djangoproject.com/) (Python)
-   **Frontend**: HTML5, CSS3, [Bootstrap 5](https://getbootstrap.com/)
-   **Database**: PostgreSQL (Production) / SQLite (Development)
-   **Media Storage**: [Cloudinary](https://cloudinary.com/)
-   **Deployment**: Setup for [Render](https://render.com/)

## ⚙️ Installation & Local Development

Follow these steps to get the project running locally.

### Prerequisites

-   Python 3.8+
-   pip (Python package manager)
-   git

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Blog_App_Python
```

### 2. Create and Activate a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the root directory (same level as `manage.py`) and add the following:

```env
DEBUG=True
SECRET_KEY=your_secret_key_here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3 # Or your local PostgreSQL URL
CLOUD_NAME=your_cloudinary_name
API_KEY=your_cloudinary_api_key
API_SECRET=your_cloudinary_api_secret
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## 🚀 Deployment

This project includes a `build.sh` script optimized for deployment on Render.

1.  Push your code to GitHub.
2.  Connect your repository to Render.
3.  Set the **Build Command** to: `./build.sh`
4.  Set the **Start Command** to: `gunicorn myproject.wsgi`
5.  Add the environment variables (DATABASE_URL, SECRET_KEY, CLOUDINARY credentials, etc.) in the Render dashboard.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
