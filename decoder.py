import json
import os

def build_and_test_decoder(json_path, test_text):
    # 1. 读取原始主表
    if not os.path.exists(json_path):
        print(f"❌ 找不到文件: {json_path}。请确保主映射表在同一文件夹下。")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        master_table = json.load(f)

    # 2. 核心逻辑：翻转字典 (CJKL字符 -> 汉字)
    # 我们只需要主表里的 cjkl_char 作为 Key，汉字作为 Value
    decoder_dict = {v['cjkl_char']: k for k, v in master_table.items()}

    # 3. 将还原字典保存，方便以后直接使用
    with open('CJKL_Decoder.json', 'w', encoding='utf-8') as f:
        json.dump(decoder_dict, f, ensure_ascii=False, indent=4)
    print("✅ 还原字典 CJKL_Decoder.json 已生成！")

    # 4. 模拟物理实验：编码器 (Encoder)
    # 把普通汉字转成 CJKL
    encoded_str = ""
    for char in test_text:
        if char in master_table:
            encoded_str += master_table[char]['cjkl_char']
        else:
            encoded_str += char # 符号、空格、不在表里的字原样保留

    # 5. 模拟物理实验：还原器 (Decoder)
    # 把 CJKL 字符转回汉字
    decoded_str = ""
    for char in encoded_str:
        if char in decoder_dict:
            decoded_str += decoder_dict[char]
        else:
            decoded_str += char

    # 6. 逻辑闭环审计
    print("\n--- 🏁 最小闭环物理实验报告 ---")
    print(f"【输入】: {test_text}")
    print(f"【密文】: {encoded_str}")
    print(f"【还原】: {decoded_str}")
    
    if test_text == decoded_str:
        print("\n🏆 逻辑闭环成功：100% 无损还原，0 信息丢失！")
    else:
        print("\n⚠️ 逻辑闭环失败：请检查原始数据是否有重复。")

# --- 执行区 ---
if __name__ == "__main__":
    # 你可以把这段话换成任何你想测试的内容
    input_text = "一乙二十丁，开始测试。" 
    build_and_test_decoder('CJKL_Master_Table.json', input_text)