const { Client } = require('pg');

const connectionString = process.env.DATABASE_URL || "postgresql://neondb_owner:npg_s8PZeYXEAFw0@ep-hidden-heart-avsyx1px-pooler.c-11.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require";

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { rollNumber, slideId, answer, isCorrect } = req.body;

  if (!rollNumber || !slideId || answer === undefined || isCorrect === undefined) {
    return res.status(400).json({ error: 'Roll number, slide ID, answer, and correctness are required.' });
  }

  const client = new Client({ connectionString });
  
  try {
    await client.connect();
    
    // Save quiz answer (ON CONFLICT update the response)
    await client.query(`
      INSERT INTO quiz_responses (roll_number, slide_id, answer, is_correct, submitted_at)
      VALUES ($1, $2, $3, $4, CURRENT_TIMESTAMP)
      ON CONFLICT (roll_number, slide_id)
      DO UPDATE SET answer = EXCLUDED.answer, is_correct = EXCLUDED.is_correct, submitted_at = CURRENT_TIMESTAMP;
    `, [rollNumber.trim().toUpperCase(), slideId, String(answer), isCorrect]);

    return res.status(200).json({ success: true, message: 'Response recorded successfully!' });
  } catch (error) {
    console.error("Quiz submission error:", error);
    return res.status(500).json({ error: 'Internal server error: ' + error.message });
  } finally {
    await client.end();
  }
}
