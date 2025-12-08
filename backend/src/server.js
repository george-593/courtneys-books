const express = require("express");
require("dotenv").config({ path: "../.env" });

PORT = 3000;
BASE_ROUTE = "/api";

const app = express();
const router = express.Router();

// Base Route
router.get("/", (req, res) => {
	res.send("Hello World");
});

// Start Server
app.use(BASE_ROUTE, router);
app.listen(PORT, () => {
	console.log("Server running");
});
