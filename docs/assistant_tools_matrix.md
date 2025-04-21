| Folder       | File                        | Subsystem       | Purpose                       | Enhancement                         |
|:-------------|:----------------------------|:----------------|:------------------------------|:------------------------------------|
| ui_layer     | vault_editor_tab.py         | Vault Zone      | Edits/loads assistant vaults  | GPT-powered vault recommender       |
| ui_layer     | file_stripper.py            | Stripper Deck   | Extracts logic from files     | Add toggle: function/class/inline   |
| ui_layer     | function_runner_tab.py      | Runner          | I/O sandbox for applets       | Add caching + input preset          |
| ui_layer     | dag_builder_tab.py          | Flow Builder    | Build DAGs visually           | Add GPT DAG planner                 |
| ui_layer     | blueprint_viewer_tab.py     | Viewer          | View blueprint applets        | Export to tools/core                |
| core         | dag_runner.py               | Runner          | Executes DAG flows            | Log timing + error highlight        |
| builder      | assistant_builder.py        | Exporter        | Build assistant folders       | Add pre-check + README validator    |
| exporter     | github_packager.py          | GitHub Zipper   | ZIPs assistant folder         | Push-to-repo shell integration      |
| intelligence | assistant_purpose_engine.py | GPT Classifier  | Detect assistant type         | GPT memory loop for export feedback |
| logger       | build_tracker.py            | Build Tracker   | Tracks builds, tests, exports | Visual timeline tab                 |
| logs         | function_calls.json         | Function Log    | Stores input/output runs      | Add timestamp + result field        |
| logs         | dag_runs.json               | DAG Log         | Stores DAG executions         | Add color-coded DAG status          |
| logs         | builder_log.json            | Builder History | Build + test session log      | Auto-sync to Notion                 |
| validation   | test_generator.py           | Test Generator  | Writes test_*.py              | Add GPT edge/fuzz case generation   |
| config       | manifest.json               | Manifest        | Assistant type + metadata     | Add GPT accuracy score + hash ID    |