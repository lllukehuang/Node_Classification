## Version note
1 SGD 2000 不收敛 loss2.03

2 Adam 2000 loss 2.00

3 Adam 10000 loss 1.80 大概在5000时就保持不变 -> 测试 22% test1.csv

4 Adam 初始化 5000 loss 360+ 初始化不好爆炸了

5 Adam 初始化 5000 只使用边的关系

6 Adam 初始化 5000 优化了特征提取（数量级） -> 测试7% test3.csv

7 Adam 乱拼结构 10000 lr 0.0001

8 Adam 乱拼结构 10000 lr 0.001 -> 测试16% test4.csv