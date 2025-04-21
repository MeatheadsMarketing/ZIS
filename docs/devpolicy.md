# 🧠 FILEMIND Development Policy

## 🔐 Placeholder Enforcement Policy

> As of `v2.2.1-audit-hardened`, FILEMIND will never include placeholder `.py` files in any deploy, push, or `/pages/` rebuild unless explicitly instructed.

### ✅ Policy Scope
- All `.py` files in root, `/pages/`, or `/scripts/`
- Any file flagged with:
  - Length < 100 characters
  - Contains `placeholder` (case-insensitive)
  - Lacks `import streamlit` or key logic blocks

### 🔍 What Happens
- File is **auto-flagged** during any audit
- Placeholder is replaced with correct scaffold or rebuilt from memory
- Clean versions are zipped, committed, or pushed

### 🧪 Enforcement Points
- `scan before push`
- `pages_clean builder`
- `deploy zip bundler`
- `Streamlit launch prep`

---

### 🔁 Example
```python
# BAD (placeholder)
# auto_categorizer.py – placeholder

# GOOD (real)
import streamlit as st
st.title("🧠 Auto Categorizer")
```

---

**Maintained by:** GPT-4 System Assistant, Phase 2+. Lock-in confirmed.
