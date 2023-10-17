

def is_of_type(value, target_type):
    try:
        # Try to convert the value to the target type
        target_type(value)
        return True  # Conversion was successful
    except (ValueError, TypeError):
        return False  # Conversion failed