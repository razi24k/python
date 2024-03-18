def filter_recommended_products(ids, rated, purchased):
    return set(filter(lambda r: r in rated or r in purchased, ids))


products = {
    "laptop": {
        "id": 43,
        "rate": 4.2,
        "sales": 5
    },
    "Xiaomi": {
        "id": 53,
        "rate": 4,
        "sales": 5
    },
    "clock": {
        "id": 23,
        "rate": 3.1,
        "sales": 8
    },
    "chain": {
        "id": 5,
        "rate": 1.4,
        "sales": 3
    },
    "ipad": {
        "id": 3,
        "rate": 2.4,
        "sales": 2
    }
}
all_id = []
highly_rated = []
highly_purchase = []
for i in products:
    all_id.append(products[i]["id"])
    if products[i]["rate"] > 2.5:
        highly_rated.append(products[i]["id"])
    elif products[i]["sales"] > 4:
        highly_purchase.append(products[i]["id"])
print(filter_recommended_products(all_id, highly_rated, highly_purchase))