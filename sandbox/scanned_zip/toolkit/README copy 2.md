# 🧠 FlowStack Intelligence System v5.0.0

This repository powers a modular, AI-enhanced Flow Intelligence system built to monitor, upgrade, and deploy applet-to-system workflows using Streamlit, Notion, and GitHub.

---

## 📦 Included

| File | Purpose |
|------|---------|
| `flowstack_master_v5.csv` | Tier-5 Notion-compatible tool registry |
| `flowstack_map.md` | Mermaid visual flowchart of tool dependencies |
| `flowstack_visualizer.py` | Script to regenerate Mermaid diagram |
| `flowstack_auto_refresh_enhanced.py` | Live update + rebuild + Git auto-commit system |
| `notion_sync_flowstack.py` | Pushes CSV entries to Notion DB |
| `flowstack_push.sh` | Git auto-commit + tagging script |
| `tab_flowstack_tracker.py` | Streamlit tab to view full registry |
| `tab_flowstack_visual.py` | Streamlit tab to view system map |
| `main_app.py` | Homepage for FlowStack Streamlit launcher |

---

## 🧠 How to Use

### 🔁 Run Auto-Refresh + Git Push

```bash
python flowstack_auto_refresh_enhanced.py
```

This:
- Rebuilds `flowstack_map.md` from the CSV
- Checks for `Placeholder Check = True`
- Commits updates + tags release in Git

---

### 🚀 Launch Streamlit UI

```bash
streamlit run main_app.py
```

Two tabs:
- **📊 Tracker Table:** Filterable tool grid
- **📍 Visual Map:** Mermaid diagram viewer

---

### 🔄 Sync to Notion

```bash
python notion_sync_flowstack.py
```

Uses environment variables:
- `NOTION_API_KEY`
- `NOTION_FLOWSTACK_DB_ID`

---

## 🏷 Tag

Latest release: `flowstack-v5.0.0`

---

## 🛠 Future Options

- `flowstack_rebuilder.py` for GPT-based auto-repair
- CI/CD YAML under `.github/workflows/ci_flowstack.yml`
- Export bundles, PDF summaries, and monetization triggers

---

Built to operate at **intelligence infrastructure level.**
