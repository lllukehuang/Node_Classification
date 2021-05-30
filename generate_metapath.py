import sys
import os
import random
import pandas as pd
from collections import Counter
from tqdm import tqdm

class MetaPathGenerator:
    def __init__(self):
        self.author_to_paper = dict()
        self.paper_to_author = dict()
        self.paper_to_paper = dict()

    def read_data(self, dirpath):
        with open('all_author_to_papers.txt','r') as f:
            for line in f.readlines():
                split_content = line.split(' ')
                # print(split_content)
                cur_author_id = "a"+split_content[0]
                self.author_to_paper[cur_author_id] = ["v"+split_content[1]]
                for feat_num in split_content[2:-1]:
                    self.author_to_paper[cur_author_id].append("v"+feat_num)

        with open('all_paper_to_authors.txt','r') as f:
            for line in f.readlines():
                split_content = line.split(' ')
                # print(split_content)
                cur_paper_id = "v"+split_content[0]
                self.paper_to_author[cur_paper_id] = ["a"+split_content[1]]
                for feat_num in split_content[2:-1]:
                    self.paper_to_author[cur_paper_id].append("a"+feat_num)

        with open('features/all_paper_reference.txt','r') as f:
            for line in f.readlines():
                split_content = line.split(' ')
                # print(split_content)
                cur_paper_id = "v"+split_content[0]
                self.paper_to_paper[cur_paper_id] = ["v"+split_content[1]]
                for feat_num in split_content[2:-1]:
                    self.paper_to_paper[cur_paper_id].append("v"+feat_num)

    def generate_random_aca(self, outfilename, numwalks, walklength):

        outfile = open(outfilename, 'w', encoding='utf-8')
        # 更换思路： 需要获取每个paper的path 应以paper为起点
        for paper in tqdm(self.paper_to_author):
            paper0 = paper
            for j in range(0, numwalks):  # wnum walks
                outline = str(paper0)
                for i in range(0, walklength):
                    authors = self.paper_to_author[paper]
                    numc = len(authors)
                    authorid = random.randrange(numc)
                    author = authors[authorid]
                    outline += " " + str(author)
                    papers = self.author_to_paper[author]
                    numa = len(papers)
                    paperid = random.randrange(numa)
                    paper = papers[paperid]
                    outline += " " + str(paper)
                outfile.write(outline + "\n")

        # 生成paper -> paper metapath 孤立点指向自己
        numwalks1 = 10
        walklength1 = 5

        for paper in tqdm(self.paper_to_paper):
            paper0 = paper
            for j in range(0, numwalks1):  # wnum walks
                outline = str(paper0)
                for i in range(0, walklength1):
                    # authors = self.paper_to_author[paper]
                    # numc = len(authors)
                    # authorid = random.randrange(numc)
                    # author = authors[authorid]
                    # outline += " " + str(author)
                    papers = self.paper_to_paper[paper]
                    numa = len(papers)
                    paperid = random.randrange(numa)
                    paper = papers[paperid]
                    outline += " " + str(paper)
                outfile.write(outline + "\n")
        # for author in tqdm(self.author_to_paper):
        #     author0 = author
        #     for j in range(0, numwalks):  # wnum walks
        #         outline = str(author0)
        #         for i in range(0, walklength):
        #             papers = self.author_to_paper[author]
        #             numa = len(papers)
        #             paperid = random.randrange(numa)
        #             paper = papers[paperid]
        #             outline += " " + str(paper)
        #             authors = self.paper_to_author[paper]
        #             numc = len(authors)
        #             authorid = random.randrange(numc)
        #             author = authors[authorid]
        #             outline += " " + str(author)
        #         outfile.write(outline + "\n")
        outfile.close()


# python py4genMetaPaths.py 1000 100 net_aminer output.aminer.w1000.l100.txt
# python py4genMetaPaths.py 1000 100 net_dbis   output.dbis.w1000.l100.txt

# dirpath = "net_aminer"
# OR
# dirpath = "net_dbis"
dirpath = '.'
# numwalks = int(sys.argv[1])
numwalks = 10 # 每个节点所随机游走的次数
# numwalks = 1 # 每个节点所随机游走的次数
# walklength = int(sys.argv[2])
walklength = 5 # 每次走的总长度 (conf 起头, 一次：走两个节点（author conf）)
# walklength = 1 # 每次走的总长度 (conf 起头, 一次：走两个节点（author conf）)

# dirpath = sys.argv[3]
# outfilename = sys.argv[4]
# outfilename = "test_metapath.txt"
outfilename = "features/graph_metapath_total_v1.txt"


def main():
    mpg = MetaPathGenerator()
    mpg.read_data(dirpath)
    mpg.generate_random_aca(outfilename, numwalks, walklength)


if __name__ == "__main__":
    main()
