# Personal Dashboard

A personal morning briefing dashboard built with Streamlit.

## Features

- **Morning Brief**: Health (Whoop), Finance (HOOD), Weather, News
- **Finance Tracker**: Stock watchlist with charts
- **Health Log**: Recovery, sleep, weight tracking
- **Responsive**: Mobile-friendly layout

## Run Locally

```bash
pip install -r requirements.txt

# Optional: Copy and configure secrets
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit .streamlit/secrets.toml

streamlit run app.py
```

Open http://localhost:8501

## Data Integrations

- **Whoop**: Connect API for automatic health sync
- **Stocks**: Yahoo Finance for real-time prices
- **Weather**: OpenWeatherMap (optional)

## Deploy

### Streamlit Cloud (Free)

1. Push to GitHub
2. Go to https://streamlit.io/cloud
3. Deploy from repo
4. Add secrets in Settings

### Docker

```bash
docker-compose up -d
```

## Roadmap

- [ ] Whoop API integration
- [ ] Real weather data
- [ ] Daily notes/journal
- [ ] Workout logging
- [ ] More stock tickers
