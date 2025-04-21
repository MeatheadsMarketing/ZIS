
import streamlit as st
import os
import ast
import pandas as pd
from gpt_logic_evaluator import set_api_key, gpt_analyze_script
from recovery_logger import log_recovery_snapshot

REGISTRY_PATH = "registry/component_registry.csv"
SHORTCUT_PATH = "shortcuts/shortcut_registry_batch_05.csv"

if "last_role" not in st.session_state:
    st.session_state.last_role = "Utility"

def extract_defs_from_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
        return [n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
    except Exception:
        return []

def is_registered(component):
    if os.path.exists(REGISTRY_PATH):
        df = pd.read_csv(REGISTRY_PATH)
        return component in df["Component"].values
    return False

def recovered_tools_launcher_tab():
    st.title("🧠 Recovered Tools Launcher")
    st.caption("Review and register recovered logic — with GPT-powered tagging and shortcuts.")

    base_dir = "RecoveredTools_Library_Categorized"
    if not os.path.exists(base_dir):
        st.warning("No categorized tool directory found.")
        return

    categories = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
    selected_cat = st.selectbox("Choose Tool Category", categories)
    selected_path = os.path.join(base_dir, selected_cat)
    files = [f for f in os.listdir(selected_path) if f.endswith(".py")]

    selected_file = st.selectbox("Select Tool File", files)
    full_path = os.path.join(selected_path, selected_file)

    st.markdown(f"📁 **File:** `{selected_file}`\n📂 **Category:** `{selected_cat}`\n🧩 **Registered:** `{is_registered(selected_file)}`")

    with open(full_path, "r", encoding="utf-8") as f:
        code = f.read()
    defs = extract_defs_from_file(full_path)

    with st.expander("📁 Code Preview", expanded=True):
        st.code(code, language="python")

    with st.expander("🎛️ Power Menu", expanded=False):
        launch_ready = st.checkbox("Mark as Launch-Ready")
        system_role = st.selectbox("Assign Role", ["Cleaner", "Trigger", "Planner", "Auditor", "Utility"], index=["Cleaner", "Trigger", "Planner", "Auditor", "Utility"].index(st.session_state.last_role))
        st.session_state.last_role = system_role
        suggested_shortcut = st.text_input("Suggest a Shortcut Name", placeholder="#TAG-ME")
        gpt_response = ""

        tab = st.radio("Switch Panel", ["GPT", "Export", "Run"], horizontal=True)

        if tab == "GPT":
            if st.button("🔍 GPT Suggestion"):
                set_api_key()
                gpt_response = gpt_analyze_script(code)
                st.markdown("### 🧠 GPT Suggestion")
                st.info(gpt_response)

            if st.button("💡 Apply GPT Suggestion"):
                if "role" in gpt_response.lower():
                    for r in ["Cleaner", "Trigger", "Planner", "Auditor", "Utility"]:
                        if r.lower() in gpt_response.lower():
                            system_role = r
                            st.success(f"Auto-set role to: {r}")
                            break
                if "launch" in gpt_response.lower() and "yes" in gpt_response.lower():
                    launch_ready = True
                    st.success("Auto-set Launch-Ready: ✅")

        if tab == "Export":
            if st.button("📤 Export to Registry"):
                row = {
                    "Component": selected_file,
                    "Type": "Recovered Tool",
                    "Origin": selected_cat,
                    "Status": "Launch-Ready" if launch_ready else "Pending",
                    "Tags": system_role,
                    "Shortcut": suggested_shortcut,
                    "GPT_Notes": gpt_response
                }
                log_recovery_snapshot(zip_name="manual_export", files_processed=[selected_file], gpt_summary=gpt_response, registered_components=[selected_file])
                if os.path.exists(REGISTRY_PATH):
                    df = pd.read_csv(REGISTRY_PATH)
                    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
                else:
                    df = pd.DataFrame([row])
                df.to_csv(REGISTRY_PATH, index=False)
                st.success(f"{selected_file} added to component_registry.csv.")

                if suggested_shortcut:
                    shortcut_row = {"Shortcut": suggested_shortcut, "Component": selected_file}
                    if os.path.exists(SHORTCUT_PATH):
                        sc_df = pd.read_csv(SHORTCUT_PATH)
                        sc_df = pd.concat([sc_df, pd.DataFrame([shortcut_row])], ignore_index=True)
                    else:
                        sc_df = pd.DataFrame([shortcut_row])
                    sc_df.to_csv(SHORTCUT_PATH, index=False)
                    st.success(f"Shortcut `{suggested_shortcut}` added to shortcut table.")

        if tab == "Run":
            if st.button("▶️ Run This Script"):
                st.info("Running...")
                os.system(f"python '{full_path}'")
                st.success("Script executed.")
