

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
            break
    
    out = "-".join([str(d0[i]) for i in key_list[:start]]) + "-"
    
    out += "(" + ".".join([str(d0[i]) for i in key_list[start:]])
    out += "--" + ".".join([str(d1[i]) for i in key_list[start:]]) + ")"

    return out

def extractInfo(func, spacer=","):
    attributes = [str(i) for i in list(func.__dict__.values())[:-1]]
    attrStr = spacer.join(attributes)
    hours = []
    for i in range(len(list(func.__dict__.values())[-1])):
        hours.append(formatDict([list(func.__dict__.values())[-1][i][0].getAttributes(), list(func.__dict__.values())[-1][i][1].getAttributes()]))
    hoursStr = spacer.join(hours)
    return attrStr, hoursStr
