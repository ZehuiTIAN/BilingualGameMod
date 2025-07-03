def merge_subtitles(ch_file, en_file, output_file):
    # 读取中文文件
    with open(ch_file, 'r', encoding='utf-8') as f:
        ch_lines = f.readlines()
    
    # 读取英文文件
    with open(en_file, 'r', encoding='utf-8') as f:
        en_lines = f.readlines()
    
    # 创建字典存储键值对
    ch_dict = {}
    en_dict = {}
    
    # 处理中文文件
    for line in ch_lines:
        if '%' in line and '\t' in line:
            l = line.strip().split('\t', 1)
            if len(l) != 2:
                print(f"Warning: Line '{line.strip()}' in Chinese file is not in the expected format.")
                key, value = l[0], " "
            else:
                key, value = l[0], l[1]
            ch_dict[key] = value
    
    # 处理英文文件
    for line in en_lines:
        if '%' in line and '\t' in line:
            key, value = line.strip().split('\t', 1)
            en_dict[key] = value
    
    # 合并文件
    with open(output_file, 'w', encoding='utf-8') as f:
        # 先处理所有中文文件中有的键
        for key in ch_dict:
            ch_value = ch_dict[key]
            en_value = en_dict.get(key, '')  # 获取对应的英文，如果没有则为空
            if en_value:
                merged_line = f"{key}\t{ch_value}({en_value})\n"
            else:
                print(f"Warning: Key '{key}' found in Chinese file but not in English file.")
                merged_line = f"{key}\t{ch_value}\n"
            f.write(merged_line)
        
        # 处理英文文件中有但中文文件中没有的键
        for key in en_dict:
            if key not in ch_dict:
                merged_line = f"{key}\t({en_dict[key]})\n"
                print(f"Warning: Key '%s' found in English file but not in Chinese file.\n" % key)
                f.write(merged_line)

# 使用示例
merge_subtitles('backup/lang_ch.ini', 'backup/lang_en.ini', 'ch-en.ini')