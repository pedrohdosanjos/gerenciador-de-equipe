

def is_of_type(value, target_type):
    try:
        # Try to convert the value to the target type
        target_type(value)
        return True  # Conversion was successful
    except (ValueError, TypeError):
        return False  # Conversion failed

def formatDict(period):
    d0, d1 = period
    start = 0
    key_list = list(d0.keys())
    for key in key_list:
        if d0[key] != d1[key]:
            start = key_list.index(key)
    
    out = "-".join([str(d0[i]) for i in key_list[:start]]) + "-"
    
    out += "(" + ".".join([str(d0[i]) for i in key_list[start:]])
    out += " -- " + ".".join([str(d1[i]) for i in key_list[start:]]) + ")"

    return out