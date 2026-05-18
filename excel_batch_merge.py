import os
import pandas as pd

def batch_merge_excel():
    # 1. 创建待合并文件夹
    folder_name = "待合并文件"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"✅ 已自动创建「{folder_name}」文件夹，请把要合并的Excel文件放进去，然后重新运行脚本")
        return

    # 2. 获取文件夹里的所有Excel文件
    files = [f for f in os.listdir(folder_name) if f.endswith(('.xlsx', '.xls'))]
    if not files:
        print("❌ 文件夹里没有找到Excel文件，请检查后重试")
        return

    # 3. 批量读取并合并文件
    all_data = []
    for file in files:
        file_path = os.path.join(folder_name, file)
        df = pd.read_excel(file_path)
        df["来源文件"] = file  # 标记每条数据来自哪个文件
        all_data.append(df)

    # 4. 合并并保存结果
    merged_df = pd.concat(all_data, ignore_index=True)
    merged_df.to_excel("合并结果.xlsx", index=False)
    print(f"✅ 合并完成！共处理{len(files)}个文件，合并结果已保存为「合并结果.xlsx」")

if __name__ == "__main__":
    batch_merge_excel()