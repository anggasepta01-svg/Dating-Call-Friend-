# Dating App - Blind Chat System 💕

Aplikasi Dating Real-Time dengan Blind Chat System - Anonymous Messaging sebelum reveal identity.

## 🎯 Fitur Utama

- **Blind Chat** - Chat anonim sebelum reveal profile
- **Real-Time Messaging** - Socket.io untuk instant messaging
- **Video Call** - Integrasi video call (Agora/Twilio)
- **User Profiles** - Swipe & Match System
- **Coin System** - Top up koin dan spending coins untuk fitur premium
- **Notifications** - Push notification real-time
- **Payment Gateway** - Premium features & Coin Top-up
- **Admin Dashboard** - Manage users & reports

## 📁 Struktur Project

```
Dating-Call-Friend-/
├── backend/                    # Server Node.js
│   ├── models/                # Database models
│   ├── controllers/           # Logic handlers
│   ├── routes/               # API routes
│   ├── sockets/              # Socket.io events
│   ├── middleware/           # Auth & validation
│   ├── utils/                # Helper functions
│   ├── server.js             # Main server
│   └── package.json          # Dependencies
├── mobile/                     # React Native App
│   ├── src/
│   │   ├── screens/          # App screens
│   │   ├── components/       # Reusable components
│   │   ├── redux/            # State management
│   │   ├── services/         # API services
│   │   └── App.js            # Main app
│   └── package.json
├── docker-compose.yml
├── .env.example
└── README.md
```

## 🚀 Quick Start

### Backend
```bash
cd backend
npm install
cp .env.example .env
npm run dev
```

### Mobile
```bash
cd mobile
npm install
npm start
```

## 🔧 Tech Stack

**Backend:**
- Node.js + Express
- Socket.io (Real-time)
- MongoDB
- JWT Authentication
- Stripe Payment
- Coin System

**Mobile:**
- React Native
- Redux (State management)
- Socket.io Client
- React Navigation

## 💰 Coin System

- Users dapat top-up coins via payment gateway
- Coins digunakan untuk fitur premium: reveal photo, boost profile, super like
- Admin dapat manage coin packages
- Real-time coin balance updates

## 📚 Documentation

Lihat folder `/docs` untuk:
- API Documentation
- Database Schema
- Installation Guide
- Coin System Guide

## 👥 Contributors

- Angga Septa
