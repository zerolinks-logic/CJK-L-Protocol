import json
import os

def run_audit():
    # 自动搜索当前目录下所有的 json 文件
    json_files = [f for f in os.listdir('.') if f.endswith('.json')]
    if not json_files:
        print("❌ 错误：没找到任何 JSON 资产文件！")
        return
    
    target = json_files[0] # 默认取第一个
    print(f"🔍 正在审计资产：{target}")
    
    with open(target, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    all_chars = [v['cjkl_char'] for v in data.values()]
    unique_chars = set(all_chars)
    collisions = len(all_chars) - len(unique_chars)
    
    print("-" * 30)
    print(f"✅ 审计完成！")
    print(f"📊 汉字总数: {len(data)}")
    if collisions == 0:
        print(f"🛡️ 逻辑状态: 完美 (0 碰撞)！你的坐标系是无懈可击的。")
    else:
        print(f"⚠️ 逻辑状态: 发现 {collisions} 个碰撞点，需要微调算法。")
    print("-" * 30)

if __name__ == "__main__":
    run_audit()