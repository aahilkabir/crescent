const { Client } = require('pg');

const connectionString = "postgresql://neondb_owner:npg_s8PZeYXEAFw0@ep-hidden-heart-avsyx1px-pooler.c-11.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require";

async function main() {
  const client = new Client({ connectionString });
  await client.connect();

  console.log("Connected to Neon Database successfully!");

  console.log("Creating 'students' table...");
  await client.query(`
    CREATE TABLE IF NOT EXISTS students (
      id SERIAL PRIMARY KEY,
      roll_number VARCHAR(50) UNIQUE NOT NULL,
      name VARCHAR(100) NOT NULL,
      checked_in_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
  `);

  console.log("Creating 'quiz_responses' table...");
  await client.query(`
    CREATE TABLE IF NOT EXISTS quiz_responses (
      id SERIAL PRIMARY KEY,
      roll_number VARCHAR(50) NOT NULL,
      slide_id VARCHAR(100) NOT NULL,
      answer VARCHAR(255) NOT NULL,
      is_correct BOOLEAN NOT NULL,
      submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      CONSTRAINT unique_student_quiz UNIQUE(roll_number, slide_id)
    );
  `);

  console.log("Creating 'code_submissions' table...");
  await client.query(`
    CREATE TABLE IF NOT EXISTS code_submissions (
      id SERIAL PRIMARY KEY,
      roll_number VARCHAR(50) NOT NULL,
      challenge_id VARCHAR(100) NOT NULL,
      code_content TEXT NOT NULL,
      submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      CONSTRAINT unique_student_challenge UNIQUE(roll_number, challenge_id)
    );
  `);

  console.log("All tables created successfully!");
  await client.end();
}

main().catch(err => {
  console.error("Database initialization failed:", err);
  process.exit(1);
});
