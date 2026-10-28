import pandas as pd
# 假设有 5 个人，分别参加了 4 门课程，获得了对应的分数
data = {'name' : pd.Series(['Alice', 'Bob', 'Cathy', 'Dany', 'Ella']),
        'Math_A' : pd.Series([1.1, 2.2, 3.3, 4.4, 5]),
        'English_A' : pd.Series([3, 2.6, 2, 1.7, 3]),
        'Math_B' : pd.Series([1.7, 2.5, 3.6, 2.4, 5]),
        'English_B' : pd.Series([5, 2.6, 2.4, 1.3, 3]),
     }

df = pd.DataFrame(data)
print(df)
