feature_dict = {}
# with open('features/metapath_total_512_ABC.txt', 'r') as f:
with open('features/test333.txt', 'r') as f:
    f.readline()
    f.readline()
    for line in f.readlines():
        split_content = line.split(' ')
        split_txt = split_content[0]
        if split_txt[0] == 'a':
            continue
        cur_paper_id = int(split_txt[1:])
        feature_dict[cur_paper_id] = [float(split_content[1])]
        for feat_num in split_content[2:-1]:
            feature_dict[cur_paper_id].append(float(feat_num))

with open('features/total_feature_ml.txt', 'a+') as f:
    for key in range(24251):
        f.write(str(key) + ' ')
        cur_feature_length = len(feature_dict[key])
        for feat in feature_dict[key]:
            f.write(str(feat) + ' ')
        f.write("\n")