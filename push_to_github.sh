#!/bin/bash

# Git Config
git config --global user.email "mmshopify2024@gmail.com"
git config --global user.name "MeatheadsMarketing"

# Navigate to the correct folder
cd ~/Desktop/ZIP_Intelligence_System || exit

# Add the ZIP to the Git index
git add ZIS_v2.0_final.zip

# Commit with your deployment message
git commit -m "🔒 Lock and Deploy ZIS v2.0"

# Push to the main branch
git push origin main
