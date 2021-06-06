import os

total_results = os.listdir('mid_result')

total_res = {}
for i in total_results:
    if i == 'readme.md':
        continue
    if i[0:5] == 'final':
        continue
    cur_path = "mid_result/" + i
    print(cur_path)
    with open(cur_path,"r",encoding='utf-8') as f:
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
with open('mid_result/final_11.txt',"a+") as f:
    for key in total_res:
        f.write(str(key)+" ")
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
            f.write(str(max_keep)+"\n")
        else:
            f.write(str(first_keep)+"\n")


