# Personal Dashboard

A personal morning briefing dashboard built with Streamlit.

## Features

- **Morning Brief**: Health (Whoop), Finance (HOOD), Weather, News
- **Finance Tracker**: Stock watchlist with charts
- **Health Log**: Recovery, sleep, weight tracking
- **Responsive**: Mobile-friendly layout
- **Secure**: Password protection with rate limiting

## Quick Start

```bash
pip install -r requirements.txt

# Set up secrets
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit .streamlit/secrets.toml - generate a password hash

streamlit run app.py
```

## Setting Up Authentication

1. Generate a password hash:
```bash
python3 -c "import hashlib; print(hashlib.sha256('your-password'.encode()).hexdigest())"
```

2. Copy the hash into `.streamlit/secrets.toml`:
```toml
APP_PASSWORD_HASH = "your-hash-here"
```

3. Restart the app

## Data Integrations

- **Whoop**: Connect API for automatic health sync
- **Stocks**: Yahoo Finance for real-time prices
- **Weather**: OpenWeatherMap (optional)

## Deploy

### Streamlit Cloud (Free)

1. Push to GitHub
2. Go to https://streamlit.io/cloud
3. Deploy from repo
4. **Important**: Add secrets in Settings → Secrets:
   ```toml
   APP_PASSWORD_HASH = "your-hash-here"
   ```

### Docker

```bash
# Copy and edit environment variables
cp .env.example .env
# Edit .env with strong passwords

docker-compose up -d
```

## Security Notes

- ✅ Passwords are hashed (SHA-256)
- ✅ Rate limiting (5 attempts, 5 min lockout)
- ✅ Session timeout (30 minutes)
- ✅ SQL injection protection
- ✅ Secrets excluded from git

## Roadmap

- [ ] Whoop API integration
- [ ] Real weather data
- [ ] Daily notes/journal
- [ ] Workout logging
- [ ] More stock tickers
