import streamlit as st
import subprocess
import os

st.title("🔐 Assistant Vault Dashboard")

st.subheader("📋 Key Status")
if st.button("Run Key Audit"):
    subprocess.run(["python", "config/test_keychain.py"])
    with open("ai_flow_engine/key_status.md", "r") as f:
        st.markdown(f.read())

st.subheader("🔁 Sync to Notion")
if st.button("Push to Notion"):
    subprocess.run(["python", "config/notion_sync_keys.py"])
    st.success("✅ Synced to Notion")

st.subheader("☁️ Upload to GCP Secret Manager")
if st.button("Upload Secrets to GCP"):
    subprocess.run(["python", "config/gcp_secret_uploader.py"])
    st.success("✅ Uploaded to GCP")

st.subheader("🔐 Vault Encryption")
if st.button("Encrypt secrets.json"):
    subprocess.run(["python", "config/encrypt_vault.py"])
    st.success("✅ Encrypted → vault.enc")

if st.button("Decrypt vault.enc"):
    subprocess.run(["python", "config/decrypt_vault.py"])
    st.success("✅ Decrypted → secrets.json")