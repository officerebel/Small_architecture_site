# Portfolio Site

A modern portfolio website inspired by BIG Architecture's project showcase, built with:
- **Backend**: Django + Wagtail CMS
- **Frontend**: Vue.js + Vite
- **API**: Django REST Framework for headless CMS

## 🚀 Live Demo
- **Frontend**: [Deploy to Vercel](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/portfolio-site)
- **Backend**: [Deploy to Railway](https://railway.app/new/template?template=https://github.com/yourusername/portfolio-site)

## 📁 Project Structure
```
portfolio-site/
├── backend/          # Django/Wagtail CMS
│   ├── portfolio/    # Main app
│   ├── requirements-prod.txt
│   └── railway.json
├── frontend/         # Vue.js app
│   ├── src/
│   └── package.json
└── README.md
```

## 🛠️ Local Development

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8002
```

### Frontend Setup
```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

## 🌐 Deployment

### Deploy Backend to Railway
1. Push to GitHub
2. Connect Railway to your GitHub repo
3. Set environment variables in Railway:
   - `DEBUG=False`
   - `SECRET_KEY=your-secret-key`
   - `ALLOWED_HOSTS=your-domain.railway.app`
   - `FRONTEND_URL=https://your-frontend-domain.vercel.app`

### Deploy Frontend to Vercel
1. Connect Vercel to your GitHub repo
2. Set build command: `npm run build`
3. Set output directory: `dist`
4. Set environment variable: `VITE_API_URL=https://your-backend.railway.app/api/`

## ✨ Features
- 🎨 Clean, BIG-inspired design
- 📱 Responsive layout
- 🖼️ Project galleries with image management
- ✏️ Easy content editing via Wagtail CMS
- 🔗 Headless CMS with REST API
- 🚀 Production-ready deployment setup

## 🔧 Admin Access
- **Local**: http://localhost:8002/cms/
- **Production**: https://your-backend.railway.app/cms/
- Login with superuser credentials

## 📝 Content Management
1. Login to Wagtail CMS
2. Navigate to "Pages" to edit content
3. Upload images in "Images" section
4. Create new projects under Projects page
5. All changes appear instantly on frontend