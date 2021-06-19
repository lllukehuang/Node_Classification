feature_dict = {}
with open('../features/graph.emb', 'r') as f:
    f.readline()
    for line in f.readlines():
        split_content = line.split(' ')
        cur_paper_id = int(split_content[0])
        # print(cur_paper_id)
        feature_dict[cur_paper_id] = [float(split_content[1])]
        for feat_num in split_content[2:]:
            feature_dict[cur_paper_id].append(float(feat_num))

with open('../features/refer_feature.txt', 'a+') as f:
    for key in range(24251):
        f.write(str(key)+' ')
        if key in feature_dict:
            for feat in feature_dict[key]:
                f.write(str(feat)+' ')
        else:
            f.write('0 '* 128)
        f.write("\n")