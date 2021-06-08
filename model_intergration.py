import os

total_results = os.listdir('mid_result')

ban_list = ['AB_s_res_69.txt', 'AB_s_res_99.txt', 'AB_aug_res_99.txt', 'AB_aug_res_199.txt',
            'ABC_aug_res_99.txt', 'ABC_aug_res_199.txt', 'all_final.txt', '512_1024_1024_69.txt',
            '512_1024_1024_89.txt', '512_2048_99.txt', '512_2048_129.txt']

total_res = {}
for i in total_results:
    if i == 'readme.md':
        continue
    if i[0:5] == 'final':
        continue
    if i in ban_list:
        continue
    cur_path = "mid_result/" + i
    print(cur_path)
    with open(cur_path, "r", encoding='utf-8') as f:
        for line in f.readlines():
            split_content = line.split(' ')
            # print(split_content)
            cur_paper_id = int(split_content[0])
            cur_pred_res = int(split_content[1][:-1])
            if cur_paper_id not in total_res:
                cur_dict = {cur_pred_res: 1}
                total_res[cur_paper_id] = cur_dict
            else:
                cur_dict = total_res[cur_paper_id]
                if cur_pred_res not in cur_dict:
                    cur_dict[cur_pred_res] = 1
                else:
                    cur_dict[cur_pred_res] += 1

print(total_res)
with open('mid_result/final_19_new_new.txt', "a+") as f:
    for key in total_res:
        f.write(str(key) + " ")
        cur_dict = total_res[key]
        first_keep = None
        max_pred_num = 0
        max_keep = None
        equal_flag = False
        for pred in cur_dict:
            if first_keep is None:
                first_keep = pred
            cur_pred_num = cur_dict[pred]
            if cur_pred_num > max_pred_num:
                max_pred_num = cur_pred_num
                max_keep = pred
                equal_flag = False
            elif cur_pred_num == max_pred_num:
                equal_flag = True
        if not equal_flag:
            f.write(str(max_keep) + "\n")
        else:
            f.write(str(first_keep) + "\n")
