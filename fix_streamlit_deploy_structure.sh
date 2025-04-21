#!/bin/bash

echo "🚚 Moving all necessary ZIS files to repo root..."

# Move files from FrontendFlow into the root
mv FrontendFlow/main_app_dynamic.py . 2>/dev/null
mv FrontendFlow/recovery_logger.py . 2>/dev/null
mv FrontendFlow/README.md . 2>/dev/null
mv FrontendFlow/.env.example . 2>/dev/null
mv FrontendFlow/setup_instructions.md . 2>/dev/null
mv FrontendFlow/LICENSE . 2>/dev/null
mv FrontendFlow/.gitignore . 2>/dev/null

# Move folders
mv FrontendFlow/tabs ./tabs 2>/dev/null
mv FrontendFlow/logs ./logs 2>/dev/null
mv FrontendFlow/exports ./exports 2>/dev/null
mv FrontendFlow/registry ./registry 2>/dev/null
mv FrontendFlow/injections ./injections 2>/dev/null

# Remove any __pycache__ folders
find . -type d -name "__pycache__" -exec rm -rf {} +

# Re-stage everything for commit
git add .
git commit -m "ZIS file structure flattened for Streamlit Cloud"
git push -u origin main --force