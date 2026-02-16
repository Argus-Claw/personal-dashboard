# Deploy to Streamlit Cloud (Free)

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Sign in with GitHub
4. Click "New app"
5. Select your repo
6. Main file path: `app.py`
7. Deploy!

## Secrets
In Streamlit Cloud dashboard:
- Go to app → Settings → Secrets
- Add environment variables:
  ```
  DATABASE_URL = "your_db_url"
  API_KEY = "your_key"
  ```
