# trading-ai-backend

Backend API for trading signals (FastAPI).
This repo fetches historical data (from 2015), trains models and serves predictions.

## Quick deploy (Railway)
1. Push this repo to GitHub.
2. Sign in to Railway (https://railway.app) and create a new project → Deploy from GitHub.
3. Set start command (if needed): `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Use endpoints:
   - GET /api/status
   - POST /api/train
   - GET /api/markets
   - GET /api/stocks
   - POST /api/binary/predict

## Notes
- First run downloads historical data and may take long.
- `data/` and `models/` are persisted locally on server; on free hosts they may be ephemeral.
- For heavy training consider uploading pretrained models or using a paid instance / S3 storage.
