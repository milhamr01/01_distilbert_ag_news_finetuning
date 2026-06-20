import json
from pathlib import Path

notebook_path = Path("notebooks/01_distilbert_ag_news_finetuning.ipynb")

nb = json.loads(notebook_path.read_text(encoding="utf-8"))

# Remove broken widget metadata from notebook-level metadata
if "metadata" in nb:
    nb["metadata"].pop("widgets", None)

# Remove widget-related cell metadata and widget outputs if any
for cell in nb.get("cells", []):
    if "metadata" in cell:
        cell["metadata"].pop("widgets", None)

    if "outputs" in cell:
        cleaned_outputs = []
        for output in cell["outputs"]:
            data = output.get("data", {})
            if "application/vnd.jupyter.widget-view+json" in data:
                continue
            cleaned_outputs.append(output)
        cell["outputs"] = cleaned_outputs

fixed_path = Path("notebooks/01_distilbert_ag_news_finetuning_fixed.ipynb")
fixed_path.write_text(json.dumps(nb, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Fixed notebook saved to: {fixed_path}")
