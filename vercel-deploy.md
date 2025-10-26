# Vercel Frontend Deployment Guide

## ⚡ Deploy to Vercel

### Option 1: One-Click Deploy (Recommended)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/officerebel/Small_architecture_site)

### Option 2: Manual Deploy

1. **Go to [Vercel.com](https://vercel.com)**
2. **Sign up/Login** with GitHub
3. **Click "New Project"**
4. **Import your repository**: `officerebel/Small_architecture_site`

### ⚙️ Vercel Configuration:

**Framework Preset**: `Other`
**Root Directory**: `frontend`
**Build Command**: `npm run build`
**Output Directory**: `dist`
**Install Command**: `npm install`

### 🔧 Environment Variables to Set in Vercel:

```bash
# Replace with your actual Railway backend URL
VITE_API_URL=https://your-railway-app.up.railway.app/api/
```

### 📝 Build Settings:
- **Build Command**: `npm run build`
- **Output Directory**: `dist`
- **Install Command**: `npm install`
- **Development Command**: `npm run dev`

### 🎯 After Deployment:
1. **Copy your Vercel URL** (e.g., `https://your-app.vercel.app`)
2. **Update Railway environment variables**:
   - `FRONTEND_URL=https://your-app.vercel.app`
   - `ADDITIONAL_CORS_ORIGINS=https://your-app.vercel.app`
   - `ALLOWED_HOSTS=your-railway-app.up.railway.app,localhost`

### 🔗 Your Frontend URLs:
- **Live Site**: `https://your-app.vercel.app`
- **Projects**: `https://your-app.vercel.app/projects`
- **About**: `https://your-app.vercel.app/about`