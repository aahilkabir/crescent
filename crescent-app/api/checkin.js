const { Client } = require('pg');

const connectionString = process.env.DATABASE_URL || "postgresql://neondb_owner:npg_s8PZeYXEAFw0@ep-hidden-heart-avsyx1px-pooler.c-11.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require";

export default async function handler(req, res) {
  // Set CORS headers so that it works from subdomains or different environments
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { rollNumber, name } = req.body;

  if (!rollNumber || !name) {
    return res.status(400).json({ error: 'Roll Number and Name are required.' });
  }

  const client = new Client({ connectionString });
  
  try {
    await client.connect();
    
    // Upsert student check-in
    await client.query(`
      INSERT INTO students (roll_number, name, checked_in_at)
      VALUES ($1, $2, CURRENT_TIMESTAMP)
      ON CONFLICT (roll_number)
      DO UPDATE SET name = EXCLUDED.name, checked_in_at = CURRENT_TIMESTAMP;
    `, [rollNumber.trim().toUpperCase(), name.trim()]);

    return res.status(200).json({ success: true, message: 'Check-in successful!' });
  } catch (error) {
    console.error("Check-in error:", error);
    return res.status(500).json({ error: 'Internal server error: ' + error.message });
  } finally {
    await client.end();
  }
}
