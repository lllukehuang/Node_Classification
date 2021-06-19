author_list = set()
paper_list = set()

with open('all_author_to_papers.txt', 'r') as f:
    for line in f.readlines():
        split_content = line.split(' ')
        # print(split_content)
        cur_author_id = split_content[0] + "a"
        author_list.add(cur_author_id)
        for cur_paper in split_content[1:-1]:
            cur_paper_id = cur_paper+"p"
            paper_list.add(cur_paper_id)


with open('../features/node_type.txt', "a+") as f:
    for author in author_list:
        f.write(author+" a\n")
    for paper in paper_list:
        f.write(paper + " p\n")