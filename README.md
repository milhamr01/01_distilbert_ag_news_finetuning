# Fine-Tuning DistilBERT for Text Classification

This repository was created for the **UAS Deep Learning — Fine-Tuning HuggingFace Models** assignment.

## Project Purpose

The purpose of this repository is to build an end-to-end Transformer encoder-based text classification system using HuggingFace. The project fine-tunes **DistilBERT** on the **AG News** dataset to classify news articles into four categories: **World**, **Sports**, **Business**, and **Sci/Tech**.

## Project Overview

This project covers the full deep learning NLP pipeline:

1. Dataset loading and inspection
2. Dataset schema standardization from `title` + `description` into a unified `text` column
3. Label conversion from `1–4` into `0–3`
4. Tokenization using DistilBERT tokenizer
5. Model loading using `distilbert-base-uncased`
6. Fine-tuning using HuggingFace `Trainer`
7. Evaluation using accuracy, macro F1, weighted F1, classification report, and confusion matrix
8. Inference demo using custom news-like text
9. Experiment reporting in `reports/evaluation_summary.md`

## Assignment Mapping

- **Task:** Task 1 — Encoder / BERT-family text classification
- **Architecture Type:** Encoder Transformer
- **Model Used:** DistilBERT (`distilbert-base-uncased`)
- **Dataset:** AG News (`sh0416/ag_news`)
- **Problem Type:** Multi-class text classification
- **Repository Name:** `finetuning-distilbert-text-classification`

## Repository Structure

```text
.
├── README.md
├── requirements.txt
├── notebooks/
│   └── 01_distilbert_ag_news_finetuning.ipynb
├── reports/
│   └── evaluation_summary.md

## Notebook Description

### `notebooks/01_distilbert_ag_news_finetuning.ipynb`

This notebook contains:

- theoretical explanation of DistilBERT and text classification,
- AG News dataset loading,
- dataset schema inspection and label distribution,
- conversion of `title` + `description` into a standardized `text` field,
- label offset handling from `1–4` into `0–3`,
- tokenization using `AutoTokenizer`,
- model loading using `AutoModelForSequenceClassification`,
- training configuration using `TrainingArguments`,
- fine-tuning using `Trainer`,
- validation and test evaluation,
- classification report,
- confusion matrix,
- inference demo,
- experiment summary export.

## Dataset Configuration

The AG News dataset loaded with these original columns:

```text
label, title, description
```

The notebook standardized the dataset into:

```text
label, title, description, text
```

The experiment used a lightweight subset for practical training in Google Colab with T4 GPU.

| Split | Size |
|---|---:|
| Training | 4000 |
| Validation | 1000 |
| Test | 1000 |

## Training Configuration

| Parameter | Value |
|---|---:|
| Model | `distilbert-base-uncased` |
| Epochs | 2 |
| Learning Rate | 2e-5 |
| Train Batch Size | 16 |
| Eval Batch Size | 32 |
| Weight Decay | 0.01 |
| Max Token Length | 128 |
| Hardware | T4 GPU |

## Final Results

### Validation Metrics

| Metric | Value |
|---|---:|
| Validation Loss | 0.259378 |
| Validation Accuracy | 0.918 |
| Validation Macro F1 | 0.913966 |
| Validation Weighted F1 | 0.917628 |

### Test Metrics

| Metric | Value |
|---|---:|
| Test Loss | 0.314908 |
| Test Accuracy | 0.899 |
| Test Macro F1 | 0.898809 |
| Test Weighted F1 | 0.898823 |

## Result Analysis

The fine-tuned DistilBERT model achieved **0.899 test accuracy** and approximately **0.899 macro F1-score** on the AG News test subset. This is a strong result for a lightweight subset-based experiment using only 4,000 training examples.

The best-performing class was **Sports**, with an F1-score of **0.97**. The lowest precision appeared in **Sci/Tech**, with precision **0.83**, indicating that some non-Sci/Tech examples were predicted as Sci/Tech. The **World** and **Business** classes had lower recall values around **0.85**, meaning some true examples from these classes were misclassified.

## Inference Demo Results

The trained model correctly predicted representative custom examples:

| Example Topic | Prediction |
|---|---|
| Government / international trade | World |
| Football championship | Sports |
| Stock market / earnings | Business |
| Artificial intelligence chip | Sci/Tech |

## How to Run

### Google Colab Recommended

1. Open `notebooks/01_distilbert_ag_news_finetuning.ipynb` in Google Colab.
2. Enable GPU:

```text
Runtime > Change runtime type > T4 GPU
```

3. Run all cells from top to bottom.
4. Download the executed notebook and upload it back to this repository.

### Local Environment

```bash
python -m venv venv
```

Activate the environment:

```bash
# Windows
.env\Scriptsctivate

# macOS/Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Jupyter Notebook:

```bash
jupyter notebook
```

## Identification

- **Name:** MUHAMMAD ILHAM RAYANDA
- **Class:** Deep Learning
- **NIM:** 1103223199

## Conclusion

This repository successfully implements an end-to-end DistilBERT fine-tuning pipeline for AG News text classification. The model achieved **89.9% test accuracy** and **0.898809 macro F1-score**, showing that DistilBERT is an efficient and effective encoder-based Transformer model for multi-class news classification.

## Notes

This repository is prepared as a reproducible academic deep learning project. The code is original/adapted for the assignment and is intended for learning purposes.
