def generate_self_review(output, checklist):
    review = []
    for item in checklist:
        if item.lower() in output.lower():
            review.append((item, "Pass"))
        else:
            review.append((item, "Fail"))
    return review