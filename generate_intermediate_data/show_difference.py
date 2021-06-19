import os

total_results = os.listdir('../mid_result')

total_res = {}
for i in total_results:
    # if i[0:5] != 'final':
    #     continue
    if not (i == 'final_15_new.txt' or i == 'final_19_new_new.txt'):
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