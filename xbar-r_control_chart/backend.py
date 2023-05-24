import pandas as pd
import numpy as np
from pyecharts.charts import Line
from pyecharts import options as opts

# 从CSV文件中读取数据并存储在DataFrame中
def read_data_from_csv(csv_file_path):
    df = pd.read_csv(csv_file_path)
    return df

# 提取所需的信息并生成绘制Xbar-R控制图的元数据
def xbar_r_metadata(data_df, limit_df):
    # 合并data_df和limit_df基于dimension_id列
    merged_df = pd.merge(data_df, limit_df, on='dimension_id', how='left')

    # 提取所需的列
    required_columns = ['dimension_id', 'cell_id', 'machine_id', 'machine_date', 'data', 'target', 'usl', 'lsl']
    extracted_data = merged_df[required_columns].copy()

    # 进行数据处理和转换
    # 在这里，你可以根据具体的需求进行数据清洗、转换、计算等操作

    # 按dimension_id分组计算Xbar和R
    grouped_data = extracted_data.groupby('dimension_id')
    xbar_values = grouped_data['data'].mean()
    r_values = grouped_data['data'].apply(lambda x: np.max(x) - np.min(x))

    # 将Xbar和R值添加到提取的数据中
    extracted_data['xbar'] = extracted_data['dimension_id'].map(xbar_values)
    extracted_data['r'] = extracted_data['dimension_id'].map(r_values)

    # 返回处理后的数据
    return extracted_data

def plot_xbar_r_chart(data_df):
    x_data = data_df['machine_date']
    xbar_data = data_df['xbar']
    r_data = data_df['r']

    line = (
        Line()
        .add_xaxis(x_data)
        .add_yaxis("Xbar", xbar_data)
        .add_yaxis("R", r_data)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Xbar-R Control Chart"),
            xaxis_opts=opts.AxisOpts(name="Date"),
            yaxis_opts=opts.AxisOpts(name="Value"),
        )
        .render("xbar_r_chart.html")
    )

# 示例用法
data_csv_file_path = 'data.csv'
limit_csv_file_path = 'limit.csv'

data_dataframe = read_data_from_csv(data_csv_file_path)
limit_dataframe = read_data_from_csv(limit_csv_file_path)

xbar_r_data = xbar_r_metadata(data_dataframe, limit_dataframe)
plot_xbar_r_chart(xbar_r_data)
