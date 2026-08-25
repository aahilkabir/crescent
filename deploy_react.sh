#!/bin/bash
# Exit immediately if a command exits with a non-zero status
set -e

echo "=== Building Vite React Slide Portal ==="
cd crescent-app
npm run build
cd ..

echo "=== Cleaning old React build chunks ==="
rm -f assets/index-*.js assets/index-*.css

echo "=== Moving production files to repository root ==="
cp crescent-app/dist/index.html ./index.html
cp crescent-app/dist/assets/index-*.js ./assets/
cp crescent-app/dist/assets/index-*.css ./assets/

echo "=== Injecting database checkin overlay to static HTML slides ==="
node scripts/inject_db_client.js

echo "=== Deployment files prepared successfully! ==="
