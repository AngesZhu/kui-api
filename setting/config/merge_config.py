def merge_config(default_configs: dict, configs: dict) -> dict:
    merged_dict = {}
    # 获取重复的key
    duplicate_keys = set(default_configs.keys()) & set(configs.keys())
    # 获取不重复的key
    unique_keys = set(default_configs.keys()) ^ set(configs.keys())
    for key in duplicate_keys:
        merged_dict[key] = {**default_configs[key], **configs[key]}
    for key in unique_keys:
        merged_dict[key] = default_configs.get(key) if default_configs.get(key) else configs.get(key)
    return merged_dict
