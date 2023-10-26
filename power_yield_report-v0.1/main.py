'''
author: ashton2914
created: 2023-10-26
updated: 2023-10-26
rev: v0.1 (under development)

This is a free and open software follow MIT License
'''

import pandas as pd

def calculate_yield_and_defects(target_date, target_process):
    xls = pd.ExcelFile('data.xlsx')
    df_data = pd.read_excel(xls, 'DATA')
    df_input = pd.read_excel(xls, 'INPUT')

    df_data_filtered = df_data[(df_data['inspect_date'] == target_date) & (df_data['inspect_process'] == target_process)].copy()
    df_input_filtered = df_input[(df_input['date'] == target_date) & (df_input['input_process'] == target_process)].copy()

    total_input = df_input_filtered['input_qty'].sum()
    total_defects = df_data_filtered['defect_qty'].sum()

    yield_rate = (total_input - total_defects) / total_input
    yield_rate = round(yield_rate * 100, 2)  # 保留两位小数并转换为百分比
    print(f"当前製程良率: {yield_rate}%")

    df_data_filtered['defect_ratio'] = (df_data_filtered['defect_qty'] / total_input) * 100
    df_data_filtered['defect_ratio'] = df_data_filtered['defect_ratio'].apply(lambda x: round(x, 2))

    df_data_sorted = df_data_filtered.sort_values(by='defect_ratio', ascending=False)

    print("不良信息：")
    for index, row in df_data_sorted.iterrows():
        print(f"{row['defect_name-zh-cn']}（{row['defect_name-en-us']}）: 不良比例 {row['defect_ratio']}%")

# 使用示例
calculate_yield_and_defects('2023-10-08', 'ANO')
