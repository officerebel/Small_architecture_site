# Deployment Commands

## 1. Push to GitHub
```bash
# Replace 'yourusername' with your GitHub username
git remote add origin https://github.com/yourusername/portfolio-site.git
git branch -M main
git push -u origin main
```

## 2. Deploy Backend to Railway

1. Go to [railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your `portfolio-site` repository
5. Railway will auto-detect it's a Django app
6. Set these environment variables in Railway:
   ```
   DEBUG=False
   SECRET_KEY=your-super-secret-key-here
   USE_SQLITE=False
   ALLOWED_HOSTS=your-app-name.railway.app
   FRONTEND_URL=https://your-frontend-domain.vercel.app
   WAGTAILADMIN_BASE_URL=https://your-app-name.railway.app
   ```

## 3. Deploy Frontend to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Set these settings:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
5. Add environment variable:
   ```
   VITE_API_URL=https://your-railway-app.railway.app/api/
   ```

## 4. After Deployment

1. **Create superuser** in Railway:
   - Go to Railway dashboard
   - Open your app's terminal
   - Run: `python manage.py createsuperuser`

2. **Access admin**:
   - Backend admin: `https://your-railway-app.railway.app/cms/`
   - Frontend: `https://your-vercel-app.vercel.app/`

## 5. Update CORS Settings

After deployment, update your Railway environment variables:
```
FRONTEND_URL=https://your-actual-vercel-domain.vercel.app
ADDITIONAL_CORS_ORIGINS=https://your-actual-vercel-domain.vercel.app
```