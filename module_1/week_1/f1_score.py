# Caculate F1-score

# Note
# TP (True Positive): Correctly identified positive cases.
# FP (False Positive): Incorrectly identified positive cases (actually negative).
# FN (False Negative): Incorrectly identified negative cases (actually positive).

def f1_score(tp,fp,fn):
    if not isinstance(tp,int):
        print("tp must be integer")
    elif not isinstance(fp,int):
        print("fp must be integer")
    elif not isinstance(fn,int):
        print("fn must be integer")
    elif tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
    else:
        precision = tp/ (tp + fp)
        recall = tp / (tp + fn)
        f1 = 2 * precision * recall / (precision + recall)
        print(f"Precision is: {precision}")
        print(f"Recall is: {recall}")
        print(f"F1-score is: {f1}")

# test
f1_score(tp=2, fp=3, fn=4)

f1_score(tp="a", fp=3, fn=4)

f1_score(tp=2, fp="a", fn=4)

f1_score(tp=2, fp=3, fn="a")

f1_score(tp=2, fp=3, fn=0)

f1_score(tp=2.1, fp=3, fn=0)