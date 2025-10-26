# Railway Backend Deployment Guide

## 🚂 Deploy to Railway

### Option 1: One-Click Deploy (Recommended)
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/django)

### Option 2: Manual Deploy

1. **Go to [Railway.app](https://railway.app)**
2. **Sign up/Login** with GitHub
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Choose your repository**: `officerebel/Small_architecture_site`
6. **Railway will auto-detect Django**

### 🔧 Environment Variables to Set in Railway:

```bash
# Required for production
DEBUG=False
SECRET_KEY=your-super-secret-production-key-here-make-it-long-and-random
USE_SQLITE=False

# Railway will provide DATABASE_URL automatically when you add PostgreSQL
# No need to set DATABASE_URL manually

# Domain settings (update after deployment)
ALLOWED_HOSTS=your-app-name.up.railway.app
WAGTAILADMIN_BASE_URL=https://your-app-name.up.railway.app

# CORS settings (update after frontend deployment)
FRONTEND_URL=https://your-frontend-app.vercel.app
ADDITIONAL_CORS_ORIGINS=https://your-frontend-app.vercel.app
```

### 📦 Add PostgreSQL Database:
1. In Railway dashboard, click **"+ New"**
2. Select **"Database"** → **"PostgreSQL"**
3. Railway will automatically set DATABASE_URL

### 🎯 After Deployment:
1. **Create superuser**: In Railway terminal run:
   ```bash
   python manage.py setup_initial_data
   ```
2. **Access admin**: `https://your-app-name.up.railway.app/cms/`
3. **Login**: admin / changeme123 (change this!)

### 🔗 Your Backend URLs:
- **API**: `https://your-app-name.up.railway.app/api/`
- **Admin**: `https://your-app-name.up.railway.app/cms/`
- **Django Admin**: `https://your-app-name.up.railway.app/admin/`