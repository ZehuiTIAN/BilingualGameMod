import json

def merge_bilingual_subtitles(en_file, ch_file, output_file):
    with open(en_file, 'r', encoding='utf-8') as f:
        en_data = json.load(f)
    
    with open(ch_file, 'r', encoding='utf-8') as f:
        ch_data = json.load(f)
    
    merged_data = {
        "$id": en_data["$id"],
        "strings": {}
    }
    
    for key in en_data["strings"]:
        en_text = en_data["strings"].get(key, "")
        ch_text = ch_data["strings"].get(key, "")
        
        # if texts are identical, use one of them
        if en_text == ch_text:
            merged_text = en_text
        else:
            # or merge them with a space in between
            merged_text = f"{en_text} {ch_text}".strip()
        
        merged_data["strings"][key] = merged_text
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)

# Example usage:
# you should replace the file paths with your actual file paths
merge_bilingual_subtitles('backup/zhCN.json', 'backup/enGB.json', 'zhCN-enGB.json')