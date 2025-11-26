// Full-Stack Application: MERN & RESTful API Architecture
// Project 2: Demonstrates RESTful API design, Node.js/Express backend
// This code showcases: RESTful API Architecture, NoSQL (MongoDB) schema definition, and security middleware integration.

const express = require('express');
const mongoose = require('mongoose');
const helmet = require('helmet'); // Security middleware (Secure by Design)
const rateLimit = require('express-rate-limit'); // Security (Vulnerability Identification)

const app = express();
const PORT = 3000;

// --- 1. SECURITY & DATA HANDLING MIDDLEWARE ---
// Use Helmet for standard security headers
app.use(helmet()); 
// Rate limiting to prevent simple DoS/brute force attacks on endpoints
const apiLimiter = rateLimit({
    windowMs: 15 * 60 * 1000, 
    max: 100, 
    message: "Too many requests from this IP, please try again after 15 minutes"
});
app.use('/api/', apiLimiter);

app.use(express.json());

// Mock MongoDB Connection (NoSQL Architecture)
const MONGODB_URI = 'mongodb://localhost:27017/foundational_app_db'; 

mongoose.connect(MONGODB_URI)
    .then(() => console.log('MongoDB connection successful (NoSQL Architecture).'))
    .catch(err => console.error('MongoDB connection error:', err));

// --- 2. RESTful API ENDPOINT DEFINITION ---

// Mock Schema for a Game Asset/Item
const ItemSchema = new mongoose.Schema({
    name: { type: String, required: true },
    rarity: { type: String, default: 'Common' },
    price: { type: Number, required: true }
});
const Item = mongoose.model('Item', ItemSchema);

// GET /api/items - Read All (CRUD)
app.get('/api/items', async (req, res) => {
    // Demonstrates efficient resource handling via RESTful architecture
    const items = await Item.find({});
    res.status(200).json(items);
});

// POST /api/items - Create (CRUD)
app.post('/api/items', async (req, res) => {
    try {
        // Input validation is critical for 'Secure by Design'
        if (!req.body.name || !req.body.price) {
            return res.status(400).json({ message: "Missing item name or price." });
        }
        const newItem = new Item(req.body);
        await newItem.save();
        res.status(201).json(newItem);
    } catch (error) {
        res.status(500).json({ message: "Error creating item." });
    }
});

app.get('/', (req, res) => {
    res.send('Full-Stack Backend is running. Access API at /api/items');
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
