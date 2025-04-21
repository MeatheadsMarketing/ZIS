#!/bin/bash

# Load environment variables
source .env

# Set variables
REPO_DIR="."
COMMIT_MSG="Update: FlowStack Intelligence System v5"
VERSION_TAG="flowstack-v5"

# Git add, commit, tag, and push
cd $REPO_DIR
git add flowstack_master_v5.csv flowstack_master_structure_v5.md tab_flowstack_tracker.py notion_sync_flowstack.py
git commit -m "$COMMIT_MSG"
git tag $VERSION_TAG
git push origin main --tags
git push origin main

echo "FlowStack v5 pushed to GitHub with tag $VERSION_TAG"
