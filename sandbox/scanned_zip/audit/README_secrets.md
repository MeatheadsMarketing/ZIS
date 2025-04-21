# 🔐 secrets.json Reference Guide

This file contains all environment keys used to power your assistant system.

## ✅ Core AI & Inference
- `OPENAI_API_KEY`: OpenAI GPT-4, GPT-4o, function calling
- `GEMINI_API_KEY`: Direct Google Gemini API
- `VERTEX_API_KEY`: GCP Vertex AI via API key
- `CLAUDE_API_KEY`: Anthropic Claude reasoning engine
- `HUGGINGFACE_TOKEN`: Access Hugging Face models and datasets
- `REPLICATE_API_TOKEN`: Run hosted models via Replicate

## 📁 Cloud Auth
- `GOOGLE_CREDENTIALS_PATH`: File path to service account
- `GOOGLE_CREDENTIALS_JSON`: Base64-encoded service account fallback

## 📊 Logs, Tasks, DevOps
- `NOTION_SECRET`: Sync logs and dashboards to Notion
- `CLICKUP_API_KEY`: Manage task flows and outputs
- `GITHUB_TOKEN`: Automate code pushes, releases, logs

## 📬 Alerts + Communication
- `SLACK_BOT_TOKEN`: Send Slack messages
- `TWILIO_ACCOUNT_SID` / `TWILIO_AUTH_TOKEN`: SMS/voice notifications

## 🧠 Vector DBs & Long-Term Memory
- `PINECONE_API_KEY` / `PINECONE_ENVIRONMENT`: Embedding memory and search
- `WEAVIATE_API_KEY` / `WEAVIATE_URL`: Open-source vector database

## 🧩 Webhooks + Sync
- `ZAPIER_WEBHOOK_URL`: Trigger Zapier flows from assistants

## 📤 Delivery & Reports
- `SENDGRID_API_KEY`: Email delivery for logs or PDFs
- `SMTP_EMAIL` / `SMTP_PASSWORD`: Use custom SMTP instead of SendGrid

## 💵 Monetization
- `STRIPE_SECRET_KEY`: Process payments for assistant products
- `GUMROAD_API_KEY`: Automate delivery after Gumroad purchases

## 🔒 Auth
- `JWT_SECRET`: Secure internal routes or APIs
- `OAUTH_CLIENT_ID` / `OAUTH_CLIENT_SECRET`: Login with Google, Notion, etc.

## 🔧 Advanced Integrations
- `AIRTABLE_API_KEY`: Airtable data sync
- `TRELLO_TOKEN`: Board-based status pipelines
- `SUPABASE_KEY` / `SUPABASE_URL`: Postgres + storage backend
- `FIREBASE_PROJECT_ID`: For Firebase integration
- `LANGCHAIN_API_KEY`: LangChain platform access