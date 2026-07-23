````markdown name=SETUP_GUIDE.md
# 🚀 Dating Call Friend - Setup Guide

## 📋 Prasyarat

- **Node.js** v18+ dan npm
- **Docker** dan **Docker Compose**
- **Git**
- **Stripe Account** (untuk payment)
- **MongoDB** (atau gunakan Docker)

---

## 🐳 Quick Start dengan Docker

### 1. Clone Repository
```bash
git clone https://github.com/anggasepta01-svg/Dating-Call-Friend-.git
cd Dating-Call-Friend-
```

### 2. Setup Environment Variables

Buat file `.env` di folder `backend/`:
```env
NODE_ENV=development
MONGODB_URI=mongodb://admin:password123@mongodb:27017/dating_app?authSource=admin
REDIS_URL=redis://redis:6379
JWT_SECRET=your_super_secret_jwt_key_here
STRIPE_SECRET_KEY=sk_test_your_stripe_secret_key
STRIPE_PUBLISHABLE_KEY=pk_test_your_stripe_publishable_key
FRONTEND_URL=http://localhost:3000
PORT=5000
```

### 3. Start Services
```bash
docker-compose up -d
```

**Output:**
- MongoDB: `mongodb://localhost:27017`
- Redis: `localhost:6379`
- Backend: `http://localhost:5000`
- Frontend: `http://localhost:3000`

### 4. Check Health
```bash
curl http://localhost:5000/health
```

---

## 🎯 Manual Setup (Tanpa Docker)

### Backend Setup

#### 1. Install Dependencies
```bash
cd backend
npm install
```

#### 2. Setup Environment
Buat `.env`:
```env
NODE_ENV=development
MONGODB_URI=mongodb://localhost:27017/dating_app
REDIS_URL=redis://localhost:6379
JWT_SECRET=your_secret_key
STRIPE_SECRET_KEY=sk_test_xxx
PORT=5000
```

#### 3. Start MongoDB & Redis
```bash
# macOS (with Homebrew)
brew services start mongodb-community
brew services start redis

# Linux
sudo systemctl start mongod
sudo systemctl start redis-server
```

#### 4. Run Backend
```bash
npm start
```

Backend running di: `http://localhost:5000`

### Frontend Setup (React Native)

#### 1. Install Dependencies
```bash
cd frontend
npm install
```

#### 2. Setup Environment
Buat `.env`:
```env
EXPO_PUBLIC_API_URL=http://localhost:5000
```

#### 3. Start Expo
```bash
npm start
```

Pilih platform:
- Press `i` untuk iOS simulator
- Press `a` untuk Android emulator
- Scan QR code untuk Expo Go app

---

## 📱 API Endpoints

### Authentication
- `POST /api/auth/register` - Register user
- `POST /api/auth/login` - Login user
- `POST /api/auth/logout` - Logout

### Coins
- `GET /api/coins/balance` - Get user balance
- `GET /api/coins/packages` - Get all coin packages
- `POST /api/coins/topup` - Create topup transaction
- `GET /api/coins/transactions` - Get transaction history
- `POST /api/coins/verify` - Verify Stripe payment

### Creator Earning
- `GET /api/creator/wallet` - Get creator wallet
- `POST /api/creator/gift` - Send gift to creator
- `GET /api/creator/analytics` - Get analytics
- `POST /api/creator/withdraw` - Request withdrawal
- `GET /api/creator/withdrawals` - Get withdrawal history

---

## 🧪 Testing

### 1. Health Check
```bash
curl http://localhost:5000/health
```

### 2. Get Coin Packages
```bash
curl http://localhost:5000/api/coins/packages
```

### 3. Register User
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "password123"
  }'
```

### 4. Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "password123"
  }'
```

---

## 🔑 Stripe Test Cards

### Success
- Card: `4242 4242 4242 4242`
- Exp: `12/25`
- CVC: `123`

### Decline
- Card: `4000 0000 0000 0002`
- Exp: `12/25`
- CVC: `123`

---

## 📊 Database Models

### User
- email, password, name, role (user/creator)
- createdAt, updatedAt

### Coin
- userId, totalCoins, totalSpent, totalEarned

### CoinTransaction
- userId, type, amount, purpose, status
- relatedUserId, metadata

### CreatorWallet
- userId, totalEarnings, availableBalance, pendingBalance
- bankDetails, ewalletDetails

### WithdrawalRequest
- userId, coinAmount, idrAmount, status
- bankDetails, withdrawalMethod

---

## 🚨 Troubleshooting

### MongoDB Connection Error
```bash
# Check if MongoDB is running
mongosh

# Or start with Docker
docker run -d -p 27017:27017 --name mongo mongo:latest
```

### Port Already in Use
```bash
# Find process using port 5000
lsof -i :5000

# Kill process
kill -9 <PID>
```

### Redis Connection Error
```bash
# Check if Redis is running
redis-cli ping

# Should return: PONG
```

### Docker Issues
```bash
# Stop all containers
docker-compose down

# Clean up volumes
docker-compose down -v

# Rebuild
docker-compose up --build
```

---

## 📦 Project Structure

```
Dating-Call-Friend-/
├── backend/
│   ├── models/          # Database models
│   ├── controllers/     # Business logic
│   ├── routes/          # API endpoints
│   ├── middleware/      # Auth, validation
│   ├── config/          # Configuration
│   └── server.js        # Entry point
├── frontend/
│   ├── screens/         # React Native screens
│   ├── components/      # Reusable components
│   ├── navigation/      # Stack navigator
│   └── App.js           # App entry
├── docker-compose.yml   # Docker services
└── README.md           # Documentation
```

---

## 🔗 Useful Links

- [Node.js Docs](https://nodejs.org/docs/)
- [MongoDB Docs](https://docs.mongodb.com/)
- [Stripe API Docs](https://stripe.com/docs)
- [React Native Docs](https://reactnative.dev/)
- [Docker Docs](https://docs.docker.com/)

---

## ✅ Checklist

- [ ] Clone repository
- [ ] Install Node.js v18+
- [ ] Setup environment variables
- [ ] Start Docker services
- [ ] Verify backend health
- [ ] Test coin packages endpoint
- [ ] Create test user
- [ ] Test payment flow

---

## 📞 Support

Jika ada masalah, buka Issue di GitHub:
https://github.com/anggasepta01-svg/Dating-Call-Friend-/issues

---

**Last Updated:** July 23, 2026
````
