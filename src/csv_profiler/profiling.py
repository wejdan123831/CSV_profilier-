# fucthins here 

def get_data_type(value: str) -> str:
    val = value.strip()
    if not val: return None
    try:
        float(val)
        return "number"
    except ValueError:
        return "string"
   
def is_missing(value: str | None) -> bool:
    if value is None:
        return True
    
    val = value.strip().lower()
    
    blacklist = [
        "",       
        "na",    
        "n/a",    
        "null",   
        "none",   
        "nan"     
    ]
    
    return val in blacklist
