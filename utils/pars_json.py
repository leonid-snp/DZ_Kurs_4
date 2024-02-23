import json


def creates_instance_class():
    with open("../files/products.json") as f:
        f = json.load(f)
        instance_category = []
        instance_product = []
        for elem in f:
            instance_category.append((elem["name"], elem["description"], elem["products"]))
            for el in elem["products"]:
                instance_product.append((el["name"], el["description"], el["price"], el["quantity"]))

        return instance_category, instance_product
