const express = require("express");
const router = express.Router();

const db = require("../db/db");

router.get("/", async (req, res) => {
	try {
		const result = await db.query("SELECT * FROM posts");
		res.json(result.rows);
	} catch (err) {
		console.error(err);
		res.status(500).send("Internal Server Error");
	}
});

module.exports = router;
