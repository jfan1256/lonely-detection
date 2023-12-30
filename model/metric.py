import pandas as pd

from sklearn.metrics import confusion_matrix
def get_metric(label, prediction):
    cm = confusion_matrix(label, prediction)
    TP = cm[1, 1]  # True Positives
    TN = cm[0, 0]  # True Negatives
    FP = cm[0, 1]  # False Positives
    FN = cm[1, 0]  # False Negatives

    # Calculate precision and recall for the positive class
    precision_pos = TP / (TP + FP) if (TP + FP) != 0 else 0
    recall_pos = TP / (TP + FN) if (TP + FN) != 0 else 0
    f1_pos = 2 * (precision_pos * recall_pos) / (precision_pos + recall_pos) if (precision_pos + recall_pos) != 0 else 0

    # Calculate precision and recall for the negative class
    precision_neg = TN / (TN + FN) if (TN + FN) != 0 else 0
    recall_neg = TN / (TN + FP) if (TN + FP) != 0 else 0
    f1_neg = 2 * (precision_neg * recall_neg) / (precision_neg + recall_neg) if (precision_neg + recall_neg) != 0 else 0

    # Display in a table
    metrics = pd.DataFrame({
        'Metric': ['Precision (Positive)', 'Recall (Positive)', 'F1 Score (Positive)',
                   'Precision (Negative)', 'Recall (Negative)', 'F1 Score (Negative)'],
        'Value': [precision_pos, recall_pos, f1_pos, precision_neg, recall_neg, f1_neg]
    })

    print(metrics)
    return metrics