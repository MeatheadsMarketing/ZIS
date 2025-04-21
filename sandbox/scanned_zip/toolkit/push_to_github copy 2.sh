
#!/bin/bash
# Push local Shortcut Command Center files to GitHub

read -p "Enter your GitHub repo URL (e.g., https://github.com/yourusername/Shortcut_Command_Center.git): " repo_url

git init
git add .
git commit -m "Initial Shortcut Command Center Deployment"
git branch -M main
git remote add origin $repo_url
git push -u origin main
