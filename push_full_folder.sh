
#!/bin/bash

# Git configuration
git config --global user.email "mmshopify2024@gmail.com"
git config --global user.name "MeatheadsMarketing"

# Navigate to ZIS folder
cd ~/Desktop/MasterFlow/ZIP_Intelligence_System || exit

# Add all files in the repo (except those in .gitignore)
git add .

# Commit everything as full deploy
git commit -m "🔒 Full Deploy: ZIS v2.0 System Folder"

# Push with force to remote repo
git remote set-url origin https://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@github.com/MeatheadsMarketing/ZIS.git
git push -u origin main --force
