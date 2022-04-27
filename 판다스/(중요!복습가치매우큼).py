import pandas as pd
fe="C:/Users/dlrms/OneDrive/Desktop/answer.txt"
# pd.clipboard 는 ctrl+c 한 것을 그대로 읽어서 pd로만들어버림.
# with open(fe,mode="r",encoding="utf-8") as f:
#     data=f.read()

# data=pd.read_clipboard() # 드래그 하면 가져와 지긴하네..
# data.set_index("1",inplace=True)
# data.set_index()
# print(data)

data=pd.read_csv(fe,header=None,sep="\t")
ans=pd.read_clipboard()
data=pd.DataFrame(data)

ans=pd.DataFrame(ans).rename(columns={"문제번호":0,"정답":1})

score=0
# print(data)
# print(ans)
for i in range(len(data[0])):
    # print(data[i][1],ans[i][1])
    if data.iloc[i][1]==ans.iloc[i][1]:
        print(data.iloc[i][1],ans.iloc[i][1])
        score+=4

print(score)
# ---- 오진영

# print(score)
# answer.txt를 읽어서 답지를 가져오기
# 탭으로 분리된(tsv) .txt 텍스트파일 불러오기
# data = pd.read_csv('파일경로', sep = "\t", , engine='python', encoding = "인코딩방식")
# data = pd.read_csv('C:/Python/answer.txt', header = None, sep = "\t", encoding = "cp949")
# data.columns = ['문제번호', '답']

# # 제출한 답지(answer_yoo.pdf)를 읽어오기(복사하기)
# df = pd.read_clipboard()
# df.columns = ['문제번호', '제출한답']

# # 채점하기
# df2 = pd.merge(df, data, on = '문제번호')
# df2.set_index('문제번호', drop=True, inplace=True)

# (df2.iloc[:,0] == df2.iloc[:,1]).sum() * 4


# 김원익
# df = pd.read_clipboard()
# df

# answer = pd.read_clipboard(header = None, names = ['문제번호', '정답'])
# answer

# mark = 0
# for i in range(len(answer)):
#     if df.iloc[i, 1] == answer.iloc[i, 1]:
#         print(f"문제 {i+1}번 정답")
#         mark += 4
#     else:
#         print(f"문제 {i+1}번 오답")
# print(f"총점: {mark}")
