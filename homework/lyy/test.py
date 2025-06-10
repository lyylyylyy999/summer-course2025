import numpy as np
from scipy import sparse
import time

# 创建一个1000阶的稀疏矩阵（对角占优）
n = 1000
data = np.ones((3, n))  # 三条对角线上的数据
data[0, :] = 2  # 上对角线
data[1, :] = 4  # 主对角线
data[2, :] = 2  # 下对角线
offsets = [-1, 0, 1]  # 对角线的偏移量
sparse_matrix = sparse.spdiags(data, offsets, n, n, format='csr')
print(sparse_matrix)

# 创建一个随机向量用于乘法运算
x = np.random.rand(n)

# 稀疏矩阵乘法并计时
start_time = time.time()
sparse_result = sparse_matrix.dot(x)
sparse_time = time.time() - start_time
print(f"稀疏矩阵乘法耗时: {sparse_time:.6f} 秒")

# 将稀疏矩阵转为稠密矩阵并进行乘法运算
dense_matrix = sparse_matrix.todense()
start_time = time.time()
dense_result = dense_matrix.dot(x)
dense_time = time.time() - start_time
print(f"稠密矩阵乘法耗时: {dense_time:.6f} 秒")

# 计算效率提升倍数
speedup = dense_time / sparse_time
print(f"稀疏矩阵乘法比稠密矩阵快 {speedup:.2f} 倍")