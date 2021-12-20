
def sort_by_price_ascending(json_string):
    groceries = {}
    item_loaded = None
    json_str = clean_json(json_string)
    for element in json_str.strip().split(','):
        for item in element.split(':'):
            if item != '"name"' and item != '"price"' and not containsDigit(item):
                 if isinstance(item,str):
                     groceries[item] = None
                     item_loaded = item
            if containsDigit(item):
                groceries[item_loaded] = item
                item_loaded = None

    return({k: v for k, v in sorted(groceries.items(), key=lambda item: item[1])})
        
                
def containsDigit(str):
    for c in str:
        return c.isdigit()
    return False

def clean_json(json_str):
    return json_str.replace("[","").replace("]","").replace("{","").replace("}","")


print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))

                
def containsDigit(str):
    for c in str:
        return c.isdigit()
    return False

def clean_json(json_str):
    return json_str.replace("[","").replace("]","").replace("{","").replace("}","")

print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))