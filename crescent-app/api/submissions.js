const { Client } = require('pg');

const connectionString = process.env.DATABASE_URL || "postgresql://neondb_owner:npg_s8PZeYXEAFw0@ep-hidden-heart-avsyx1px-pooler.c-11.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require";

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const client = new Client({ connectionString });
  
  try {
    await client.connect();
    
    // Fetch checked-in students
    const studentsRes = await client.query(`
      SELECT roll_number, name, checked_in_at 
      FROM students 
      ORDER BY checked_in_at DESC;
    `);

    // Fetch quiz statistics
    const statsRes = await client.query(`
      SELECT slide_id, answer, is_correct, COUNT(*) as count 
      FROM quiz_responses 
      GROUP BY slide_id, answer, is_correct;
    `);

    // Fetch raw responses for listing
    const rawResponsesRes = await client.query(`
      SELECT r.roll_number, s.name, r.slide_id, r.answer, r.is_correct, r.submitted_at 
      FROM quiz_responses r
      LEFT JOIN students s ON r.roll_number = s.roll_number
      ORDER BY r.submitted_at DESC;
    `);

    return res.status(200).json({
      students: studentsRes.rows,
      stats: statsRes.rows,
      rawResponses: rawResponsesRes.rows
    });
  } catch (error) {
    console.error("Fetch submissions error:", error);
    return res.status(500).json({ error: 'Internal server error: ' + error.message });
  } finally {
    await client.end();
  }
}
