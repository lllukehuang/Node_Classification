## Version note
1 SGD 2000 不收敛 loss2.03

2 Adam 2000 loss 2.00

3 Adam 10000 loss 1.80 大概在5000时就保持不变 -> 测试 22% test1.csv

4 Adam 初始化 5000 loss 360+ 初始化不好爆炸了

5 Adam 初始化 5000 只使用边的关系

6 Adam 初始化 5000 优化了特征提取（数量级） -> 测试7% test3.csv

7 Adam 乱拼结构 10000 lr 0.0001

8 Adam 乱拼结构 10000 lr 0.001 loss 1.0 -> 测试16% test4.csv

9 Adam 乱拼结构 10000 lr 0.001 隐藏层250维度 loss 1.0 0.97 0.94 0.90 0.87 0.87 

选取 4999 做输出 test7 -> 测试 27%
选取 1999 做输出 test8

优化输出4999 test9 -> 测试 29%

10 Adam 乱拼结构 10000 lr 0.0001 隐藏层250维度 meta feature

2999 loss 0.001 test10 感觉看上去不太好 但其实很好! -> 测试42.2%!

1999 test10_1

999 test10_2

11 同上，但完整训练版本

4999 loss 0.0001 test11 -> 测试41%

5999 loss 8.e-5

6999 loss 4.e-5

7999 loss 2.e-5

12 只使用metapath生成特征 (paper->author->paper, paper->paper) 128 维

999 loss 0.0003 test12 -> 测试42.3% 存在过拟合风险

13 同上， 但修改metapath生成特征维度为256，并修改隐藏层大小300

499 loss 0.005 test13 -> 测试44.6%