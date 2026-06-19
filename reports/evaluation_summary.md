# Evaluation Summary — DistilBERT AG News

## 1. Experiment Identity

- **Repository:** `finetuning-distilbert-text-classification`
- **Assignment:** UAS Deep Learning — Fine-Tuning HuggingFace Models
- **Task:** Task 1 — Encoder / BERT-family text classification
- **Architecture:** Encoder Transformer
- **Model:** `distilbert-base-uncased`
- **Dataset:** AG News (`sh0416/ag_news`)
- **Problem Type:** Multi-class text classification

## 2. Dataset Summary

The AG News dataset was loaded successfully from HuggingFace. The dataset version used in this experiment contained the columns:

```text
label, title, description
```

Because the model expects one input text field, the notebook standardized the schema by combining `title` and `description` into a new `text` column. The dataset labels originally used the range `1–4`, so the notebook converted labels into the model-compatible range `0–3`.

### Class Labels

| ID | Label |
|---:|---|
| 0 | World |
| 1 | Sports |
| 2 | Business |
| 3 | Sci/Tech |

### Dataset Subset Used

| Split | Size |
|---|---:|
| Training | 4000 |
| Validation | 1000 |
| Test | 1000 |

## 3. Training Configuration

| Parameter | Value |
|---|---:|
| Model | `distilbert-base-uncased` |
| Number of Labels | 4 |
| Epochs | 2 |
| Learning Rate | 2e-5 |
| Train Batch Size | 16 |
| Evaluation Batch Size | 32 |
| Weight Decay | 0.01 |
| Max Sequence Length | 128 |
| Hardware | T4 GPU |

## 4. Training Progress

| Epoch | Training Loss | Validation Loss | Accuracy | Macro F1 | Weighted F1 |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.383617 | 0.283212 | 0.911 | 0.906436 | 0.910379 |
| 2 | 0.246487 | 0.259378 | 0.918 | 0.913966 | 0.917628 |

The validation performance improved from epoch 1 to epoch 2. The validation loss decreased from **0.283212** to **0.259378**, and validation accuracy increased from **0.911** to **0.918**.

## 5. Final Validation Metrics

| Metric | Value |
|---|---:|
| Validation Loss | 0.259378 |
| Validation Accuracy | 0.918 |
| Validation Macro F1 | 0.913966 |
| Validation Weighted F1 | 0.917628 |

## 6. Final Test Metrics

| Metric | Value |
|---|---:|
| Test Loss | 0.314908 |
| Test Accuracy | 0.899 |
| Test Macro F1 | 0.898809 |
| Test Weighted F1 | 0.898823 |

## 7. Classification Report

```text
              precision    recall  f1-score   support

       World       0.94      0.85      0.89       266
      Sports       0.95      0.99      0.97       246
    Business       0.88      0.85      0.87       246
    Sci/Tech       0.83      0.91      0.87       242

    accuracy                           0.90      1000
   macro avg       0.90      0.90      0.90      1000
weighted avg       0.90      0.90      0.90      1000
```

## 8. Class-Level Analysis

- **Best class:** Sports achieved the strongest performance with precision **0.95**, recall **0.99**, and F1-score **0.97**.
- **Lowest precision:** Sci/Tech had the lowest precision at **0.83**, indicating that some examples from other classes were predicted as Sci/Tech.
- **Lower recall classes:** World and Business both had recall around **0.85**, meaning some true World and Business examples were misclassified.
- **Overall performance:** The model achieved balanced macro and weighted averages around **0.90**, meaning the model performed consistently across the four classes.

## 9. Inference Demo Analysis

The model was tested on four custom news-like sentences. The model predicted:

| Input Topic | Predicted Label | Observation |
|---|---|---|
| Government / international trade | World | Correct topic mapping |
| Football championship | Sports | Correct topic mapping |
| Stock market / earnings | Business | Correct topic mapping |
| AI chip / model training | Sci/Tech | Correct topic mapping |

## 10. Conclusion

The fine-tuned DistilBERT model achieved **0.899 test accuracy**, **0.898809 macro F1-score**, and approximately **0.898823 weighted F1-score** on the AG News test subset. These results are strong for a lightweight training setup with 4,000 training samples.

DistilBERT is suitable for this task because it provides a good balance between efficiency and classification performance. The model is significantly lighter than BERT-base while still producing strong contextual text representations. For further improvement, the experiment can be repeated using the full AG News training set, more epochs, or hyperparameter tuning.
