# IFMS Website (Django + Vue)

Local setup instructions

Backend (Django):

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Frontend (Vue, Vite):

```bash
cd frontend
npm install
npm run dev
```