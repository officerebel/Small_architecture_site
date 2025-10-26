# 🚀 Deploy Portfolio Site with Poetry

## ✅ **What's Ready:**
- ✅ Poetry configuration (`pyproject.toml`)
- ✅ Poetry lock file (`poetry.lock`)
- ✅ Railway configuration (`nixpacks.toml`)
- ✅ Startup script (`start.sh`)
- ✅ Code pushed to GitHub

## 🚂 **Deploy Backend to Railway**

### **Step 1: Deploy**
1. **Go to**: https://railway.app/new
2. **Login with GitHub**
3. **Click "Deploy from GitHub repo"**
4. **Select**: `officerebel/Small_architecture_site`
5. **Railway will detect Poetry automatically**

### **Step 2: Add PostgreSQL Database**
1. **In Railway dashboard, click "+ New"**
2. **Select "Database" → "PostgreSQL"**
3. **Railway will auto-connect it**

### **Step 3: Set Environment Variables**
```bash
DEBUG=False
SECRET_KEY=ecQiUDv82BT1WWwM0xSYmF2x7QW4V50_V9C4Pdq9b6VefgzgQbiLrD5DaS85U_D1Vrc
USE_SQLITE=False
ALLOWED_HOSTS=*.up.railway.app,localhost
WAGTAILADMIN_BASE_URL=https://your-app-name.up.railway.app
```

### **Step 4: Initialize Site Data**
After deployment, in Railway terminal:
```bash
poetry run python backend/manage.py setup_initial_data
```

## 🌐 **Deploy Frontend to Vercel**

### **Step 1: Deploy**
1. **Go to**: https://vercel.com/new
2. **Login with GitHub**
3. **Import**: `officerebel/Small_architecture_site`
4. **Set Root Directory**: `frontend`
5. **Set Build Command**: `npm run build`
6. **Set Output Directory**: `dist`

### **Step 2: Environment Variable**
```bash
VITE_API_URL=https://your-railway-app.up.railway.app/api/
```

## 🎯 **Final Configuration**

### **Update Railway CORS Settings:**
```bash
FRONTEND_URL=https://your-vercel-app.vercel.app
ADDITIONAL_CORS_ORIGINS=https://your-vercel-app.vercel.app
```

## 🔗 **Your Live URLs:**
- **Portfolio**: `https://your-vercel-app.vercel.app`
- **Admin**: `https://your-railway-app.up.railway.app/cms/`
- **API**: `https://your-railway-app.up.railway.app/api/`

## 🔑 **Default Login:**
- **Username**: `admin`
- **Password**: `changeme123`
- **⚠️ Change immediately after first login!**

---

## 🚀 **Quick Deploy Links:**

### **Backend (Railway):**
**[👉 Deploy Backend with Poetry](https://railway.app/new/template?template=https://github.com/officerebel/Small_architecture_site)**

### **Frontend (Vercel):**
**[👉 Deploy Frontend](https://vercel.com/new/clone?repository-url=https://github.com/officerebel/Small_architecture_site)**

---

## ✨ **Poetry Benefits:**
- 🔒 **Locked dependencies** for consistent builds
- 🚀 **Faster installs** with dependency resolution
- 🛡️ **Better security** with dependency verification
- 📦 **Clean dependency management**

**Your portfolio site is now ready for professional deployment with Poetry! 🎉**