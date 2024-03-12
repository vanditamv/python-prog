# Python dictionary program that involves some advanced manipulation and processing of data

def merge_dicts(dicts):
    merged_dict = {}
    for d in dicts:
        for key, value in d.items():
            if key in merged_dict:
                if isinstance(value, dict) and isinstance(merged_dict[key], dict):
                    merged_dict[key] = merge_dicts([merged_dict[key], value])
                else:
                    merged_dict[key] += value
            else:
                merged_dict[key] = value
    return merged_dict

# Example usage
dicts = [
    {'a': 1, 'b': 2, 'c': {'x': 10, 'y': 20}},
    {'a': 3, 'b': 4, 'c': {'x': 30, 'z': 40}},
    {'d': 5, 'e': 6}
]

merged_dict = merge_dicts(dicts)
print(merged_dict)
