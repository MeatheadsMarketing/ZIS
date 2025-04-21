# ✅ FILEMIND Phase 2 Test Plan

This checklist validates the core functionality of your deployed FILEMIND system via the Streamlit UI.

---

## 🧪 Test ZIP Setup

- [ ] Prepare a `.zip` file containing:
  - 2 `.txt` files
  - 2 `.md` files
  - 1 `.json` file
  - 1 `.csv` file
- [ ] File contents should include:
  - At least one `#X` or `#S1` shortcut
  - At least one assistant code like `A0012` or `T-R-LOGIC`

---

## 🔁 Step-by-Step Test Flow

### 1. 📦 `Zip Loader`
- [ ] Upload your test `.zip`
- [ ] Verify “✅ Extracted to” confirmation appears
- [ ] Confirm file list is displayed with correct paths + sizes

### 2. 📂 `Directory Visualizer`
- [ ] View folder tree and expand nested contents
- [ ] File names should match upload

### 3. 📑 `File Registry Table`
- [ ] Registry table shows all extracted files
- [ ] `zip_registry.csv` is saved automatically

### 4. 📏 `Size Tagger`
- [ ] Files are tagged as Tiny/Small/Medium/Large
- [ ] Size Tier column appears in registry

### 5. 🧠 `GPT Export Identifier`
- [ ] Detects if files resemble ChatGPT export format
- [ ] Column `GPT Export Detected` is added

### 6. 🧩 `Assistant Scanner`
- [ ] Assistant patterns are detected in `.md` or `.txt`
- [ ] `assistant_tag_map.json` is saved

### 7. 🏷️ `Manual Tag Editor`
- [ ] Add a tag (e.g., `"Important"`) to one or more files
- [ ] Tags persist after refresh

### 8. 🚦 `Output Router`
- [ ] Route 2 files to `→ Scan`, `→ Export`
- [ ] Column `Routing` shows the values correctly

### 9. 📋 `Summary Table Generator`
- [ ] Choose files to simulate summary
- [ ] Output written to `file_summaries.csv`

### 10. 📦 `Bundle Zipper`
- [ ] Select a `Cluster Group` and build a ZIP
- [ ] Confirm download works

---

## 📊 Dashboard Validation

- [ ] Load `filemind_dashboard.py`
- [ ] Metrics update (file count, tagged, routed, clustered)
- [ ] Registry table loads correctly

---

## ✅ Completion = System Validated
Once all checks pass, mark repo as `v2.0` and deploy confidently.