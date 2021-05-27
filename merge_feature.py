# 1、融合成一个模型 2、先降维再融合
# 最后决定先融合成一个feature。原则是padding到最长大小

feature_dict = {}

with open('features/refer_feature.txt', 'r') as f:
    for line in f.readlines():
        split_content = line.split(' ')
        # print(split_content)
        cur_paper_id = int(split_content[0])
        feature_dict[cur_paper_id] = [float(split_content[1])]
        for feat_num in split_content[2:-1]:
            feature_dict[cur_paper_id].append(float(feat_num))

max_length = 1

with open('features/author_feature.txt', 'r') as f:
    for line in f.readlines():
        split_content = line.split(' ')
        cur_paper_id = int(split_content[0])
        feature_dict[cur_paper_id].append(float(split_content[1])/42613)
        cur_length = 1
        for feat_num in split_content[2:-1]:
            feature_dict[cur_paper_id].append(float(feat_num)/42613)
            cur_length += 1
        if cur_length > max_length:
            max_length = cur_length

# for key in feature_dict:
#     while len(feature_dict[key]) != max_length:
#         feature_dict[key].append(0)

with open('features/total_feature_new.txt', 'a+') as f:
    for key in range(24251):
        f.write(str(key) + ' ')
        cur_feature_length = len(feature_dict[key])
        for feat in feature_dict[key]:
            f.write(str(feat) + ' ')
        if cur_feature_length != (128 + max_length):
            need_to_add = 128+max_length-cur_feature_length
            f.write('0 '*need_to_add)
        f.write("\n")

print(max_length)