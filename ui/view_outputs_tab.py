
import streamlit as st
import os
import time

def view_outputs_tab():
    st.title("📊 Recovery Outputs Viewer")
    st.caption("Browse all GPT-generated recovery exports.")

    base_path = "outputs/"
    if not os.path.exists(base_path):
        st.warning("No outputs folder found.")
        return

    files = [f for f in os.listdir(base_path) if f.endswith((".csv", ".md", ".json", ".txt"))]
    if not files:
        st.info("No export files found yet.")
        return

    st.markdown(f"### 🧾 Detected Files: `{len(files)}`")
    selected = st.selectbox("Select Output File", files)

    full_path = os.path.join(base_path, selected)
    if selected:
        stats = os.stat(full_path)
        mod_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stats.st_mtime))
        size_kb = round(stats.st_size / 1024, 2)

        st.markdown("#### 🧠 Output File Info")
        st.markdown(f"- **Name:** `{selected}`")
        st.markdown(f"- **Last Modified:** `{mod_time}`")
        st.markdown(f"- **Size:** `{size_kb} KB`")

        st.markdown("#### 📄 File Preview")
        with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        st.code(content, language="markdown" if selected.endswith(".md") else "text")

    if st.button("📥 Export a Copy to Desktop"):
        st.success(f"File `{selected}` ready for manual copy from `/outputs/`")
