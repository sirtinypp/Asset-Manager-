def mask_name(first, last, obj_id=None, is_demo=False):
    if not is_demo:
        return f"{first} {last}"
    
    # If no ID, use a hash of the name for deterministic masking
    if obj_id is None:
        obj_id = hash(f"{first}{last}")
        
    first_names = ["Officer", "Manager", "Supervisor", "Director", "Chief", "Analyst", "Specialist", "Coordinator"]
    last_initials = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    idx_f = abs(obj_id) % len(first_names)
    idx_l = abs(obj_id) % len(last_initials)
    
    return f"{first_names[idx_f]} {last_initials[idx_l]}-{abs(obj_id) % 1000:03d}"

def mask_department(name, obj_id=None, is_demo=False):
    if not is_demo:
        return name
        
    if obj_id is None:
        obj_id = hash(name)
        
    categories = ["Administrative Services", "Strategic Operations", "Technical Support", "Field Division", "Logistics Hub", "Policy Office"]
    idx = abs(obj_id) % len(categories)
    return f"{categories[idx]} {abs(obj_id) % 100:02d}"

def mask_username(username, is_demo=False):
    if not is_demo or username == "grootadmin":
        return username
    return f"user_{abs(hash(username)) % 10000:04d}"
