import json
from collections import defaultdict

def get_alpha_group(page_name):
    # Extract the actual filename without extension
    name = page_name.split('/')[-1]
    first_char = name[0].upper()
    if 'A' <= first_char <= 'D': return 'A-D'
    if 'E' <= first_char <= 'H': return 'E-H'
    if 'I' <= first_char <= 'M': return 'I-M'
    if 'N' <= first_char <= 'R': return 'N-R'
    if 'S' <= first_char <= 'U': return 'S-U'
    if 'V' <= first_char <= 'Z': return 'V-Z'
    return 'Other'

def chunk_pages_alphabetically(pages_list, parent_group_name):
    groups = defaultdict(list)
    
    # We want to keep the main landing page out of the alphabetical groups
    main_landing = None
    if pages_list and ("overview" in pages_list[0] or "introduction" in pages_list[0]):
        main_landing = pages_list[0]
        pages_list = pages_list[1:]

    for page in pages_list:
        if isinstance(page, str):
            group_name = get_alpha_group(page)
            groups[group_name].append(page)
        else:
            # If it's already a group (dict), we just leave it as is or append it
            groups['Other'].append(page)
            
    # Sort groups logically
    sorted_group_keys = ['A-D', 'E-H', 'I-M', 'N-R', 'S-U', 'V-Z', 'Other']
    
    new_group_items = []
    if main_landing:
        new_group_items.append(main_landing)
        
    for k in sorted_group_keys:
        if groups[k]:
            new_group_items.append({
                "group": k,
                "expanded": False,
                "pages": groups[k]
            })
            
    return new_group_items

def restructure_docs_json():
    with open('docs.json', 'r') as f:
        data = json.load(f)
        
    for tab in data['navigation']['tabs']:
        if 'groups' in tab:
            for group in tab['groups']:
                # Restructure Content Federation
                if group.get('group') == 'Content Federation' and len(group.get('pages', [])) > 10:
                    group['pages'] = chunk_pages_alphabetically(group['pages'], 'Content Federation')

    with open('docs.json', 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    restructure_docs_json()
    print("Done restructuring Content Federation.")
