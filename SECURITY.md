# Security Checklist for Personal Dashboard

## ✅ Already Secure

- [x] `secrets.toml` in `.gitignore` (won't be committed)
- [x] No hardcoded API keys in source code
- [x] `secrets.toml.example` is safe to commit (template only)
- [x] Password check is commented out by default

## 🔒 Additional Security Measures

### 1. Root .gitignore
Add to repo root:
```
.env
*.log
__pycache__/
*.pyc
.DS_Store
data/*.db
data/*.sqlite
```

### 2. Environment Variables (local dev)
Create `.env` file (already in .gitignore):
```
APP_PASSWORD=your_secure_password_here
OPENWEATHER_API_KEY=your_key
```

### 3. Streamlit Cloud Secrets
When deploying, add to Settings → Secrets:
```toml
APP_PASSWORD = "your_secure_password"
OPENWEATHER_API_KEY = "your_key"
WHOOP_TOKEN = "your_token"
```

### 4. Password Security
- Change default password before enabling auth
- Use 12+ characters, mix of cases/numbers/symbols
- Consider using `streamlit-authenticator` for multi-user

### 5. API Key Rotation
- Whoop token expires — set reminder to refresh
- Use separate API keys for dev/prod
- Monitor usage for unexpected spikes

### 6. Repository Visibility
- Currently public (anyone can see code)
- If adding sensitive business logic, consider private repo
- Dashboard data (Whoop, stocks) is personal — auth recommended

## 🚀 Before First Deploy

1. [ ] Enable password protection (uncomment lines in app.py)
2. [ ] Set strong password in Streamlit Cloud secrets
3. [ ] Add API keys to Streamlit Cloud secrets
4. [ ] Test auth flow
5. [ ] Share URL only with trusted people

## 📊 Data Privacy

- Whoop data: Personal health info — keep secure
- Stock positions: Financial info — don't share publicly
- Daily notes: Journal entries — private by nature

**Recommendation:** Enable auth before sharing URL.