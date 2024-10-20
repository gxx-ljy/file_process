import pandas as pd
import matplotlib.pyplot as plt

# 创建一个示例 DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}
df = pd.DataFrame(data)

# 计算图形的大小
num_rows, num_cols = df.shape
fig_width = num_cols * 1.5  # 每列宽度乘以一个系数
fig_height = num_rows * 0.5  # 每行高度乘以一个系数

# 创建一个图形对象，并设置大小
fig, ax = plt.subplots(figsize=(fig_width, fig_height))

# 将 DataFrame 绘制到图形对象上
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')
# the_table = ax.table(cellText=df.values, loc='center') # 不显示列名

# 保存为图片
plt.savefig('df_image.png', bbox_inches='tight')
