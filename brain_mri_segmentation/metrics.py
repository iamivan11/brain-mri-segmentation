from sklearn.metrics import jaccard_score, classification_report


def compute_jaccard(segmented, GT, labels=None, average="macro"):
    """Return per-region Jaccard and overall mean (sklearn)."""
    if labels is None:
        labels = [0, 1, 2, 3, 4, 5]
    pred = segmented.ravel()
    truth = GT.ravel()
    per_label = jaccard_score(truth, pred, labels=labels, average=None)
    result = {}
    for label, score in zip(labels, per_label):
        result[f"Region {label}"] = float(score)
    result["Overall"] = float(
        jaccard_score(truth, pred, labels=labels, average=average)
    )
    return result


def compute_P_R_F1(segmented, GT):
    """Print precision (P) / recall (R) / F1-Score (F1) classification report (sklearn)."""
    result = classification_report(GT.ravel(), segmented.ravel())
    print(result)
