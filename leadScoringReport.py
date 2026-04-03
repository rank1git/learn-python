leads = [
    {"name": "Alice Brown", "deal_value": 32000, "company_size": 500,
        "product": "cloud security", "years_in_business": 8},
    {"name": "Bob Smith", "deal_value": 8500, "company_size": 20,
        "product": "devtools", "years_in_business": 1},
    {"name": "Carol White", "deal_value": 18000, "company_size": 150,
        "product": "cloud security", "years_in_business": 5},
    {"name": "Dan Lee", "deal_value": 27000, "company_size": 80,
        "product": "devtools", "years_in_business": 3},
    {"name": "Eva Marsh", "deal_value": 5000, "company_size": 10,
        "product": "cloud security", "years_in_business": 1},
]


# def score_lead(lead):
#     score = 0
# deal_value = lead["deal_value"]
# company_size = lead["company_size"]
# years_in_business = lead["years_in_business"]
# product = lead["product"]

#     if deal_value > 25000:
#         score += 40
#     elif 10000 <= deal_value <= 25000:
#         score += 20
#     else:
#         score += 5

#     if company_size > 200:
#         score += 30
#     elif 50 <= company_size <= 200:
#         score += 20
#     else:
#         score += 5

#     if years_in_business > 5:
#         score += 20
#     elif 2 <= years_in_business <= 5:
#         score += 10

#     if product.lower() == "cloud security":
#         score += 10

#     return score

# stronger but longer way to write the score_lead function with less code. Use a tuple and a lookup table
# Scoring rules stored as lookup tables for easy maintenance
# Format: (threshold, points) — evaluated highest to lowest
def score_lead(lead):
    """
    Takes a lead dictionary and returns a score based on
    deal value, company size, years in business, and product.
    """
    score = 0
    deal_value = lead["deal_value"]
    company_size = lead["company_size"]
    years_in_business = lead["years_in_business"]
    product = lead["product"]
    deal_value_scores = [
        (25000, 40),
        (10000, 20),
        (0, 5)
    ]
    company_sizes = [
        (200, 30),
        (50, 20),
        (0, 5)
    ]
    lead_years_in_business = [
        (5, 20),
        (2, 10),
        (0, 0)
    ]

    for threshold, points in deal_value_scores:
        if deal_value > threshold:
            score += points
            break

    for threshold, points in company_sizes:
        if company_size > threshold:
            score += points
            break

    for threshold, points in lead_years_in_business:
        if years_in_business > threshold:
            score += points
            break

    if product.lower() == "cloud security":
        score += 10

    return score


print(score_lead(leads[1]))


def get_tier(score):
    """
    Takes a score and converts it to a tier based on where the score falls within different ranges.
    """
    if score >= 70:
        return "Platinum"
    elif 40 <= score <= 69:
        return "Gold"
    return "Bronze"


print("===== LEAD SCORING REPORT =====")
for index, lead in enumerate(sorted(leads, key=score_lead, reverse=True)):
    score = score_lead(lead)
    tier = get_tier(score)
    print(
        # :<15 means "left align and pad to 15 characters." Every name will take exactly 15 characters of space regardless of length, so the pipes line up perfectly.
        f"Rank {index + 1}: {lead['name']:<15} | Score: {score:5} | Tier: {tier}")
