import os
import importlib.util

def load_modules(base_path="modules"):
    categories = {}
    
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    for category_dir in sorted(os.listdir(base_path)):
        cat_path = os.path.join(base_path, category_dir)
        
        if os.path.isdir(cat_path) and not category_dir.startswith("__"):
            cat_name = category_dir.capitalize()
            categories[cat_name] = []
            
            for mod_file in sorted(os.listdir(cat_path)):
                if mod_file.endswith(".py") and not mod_file.startswith("__"):
                    mod_path = os.path.join(cat_path, mod_file)
                    mod_name = mod_file[:-3]
                    
                    spec = importlib.util.spec_from_file_location(mod_name, mod_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    if hasattr(module, "NAME") and hasattr(module, "execute"):
                        categories[cat_name].append({
                            "name": module.NAME,
                            "prompt": getattr(module, "PROMPT", None),
                            "execute": module.execute
                        })
    return categories

