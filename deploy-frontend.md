# Frontend Deployment Guide

## 🚀 Deploy to Vercel

### Option 1: One-Click Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/officerebel/Small_architecture_site&project-name=small-architecture-frontend&repository-name=small-architecture-frontend&root-directory=frontend)

### Option 2: Manual Deploy

1. **Go to [Vercel.com](https://vercel.com)**
2. **Sign up/Login** with GitHub
3. **Click "New Project"**
4. **Import your GitHub repository**
5. **Configure Project**:
   - **Root Directory**: `frontend`
   - **Framework Preset**: Vite
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`

### 🔧 Environment Variables to Set in Vercel:

```bash
VITE_API_URL=https://smallachitecture-production.up.railway.app/api/
```

### 🌐 Your Frontend URLs:

- **Production**: `https://your-project-name.vercel.app`
- **API Endpoint**: `https://smallachitecture-production.up.railway.app/api/`

### 📝 After Deployment:

1. **Update CORS settings** in Railway backend
2. **Test the connection** between frontend and backend
3. **Update any hardcoded URLs** if needed

## 🔗 Connect Frontend to Backend

The frontend is already configured to connect to your Railway backend at:
`https://smallachitecture-production.up.railway.app/api/`

Make sure to update the Railway backend CORS settings to allow your Vercel domain.