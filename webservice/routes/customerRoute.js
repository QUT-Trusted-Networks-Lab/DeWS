const express = require('express');
const router = express.Router();
const customers = require("../controllers/customerController");

// Create a new customer
router.post("/", customers.createNewCustomer);
// Get all customers
router.get("/all", customers.getAll);

module.exports = router;