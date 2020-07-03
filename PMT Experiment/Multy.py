import os

fp=r'C:\Users\wangjing\Homework\PMT Experiment'
os.chdir(fp)  #一定要把工作目录修改到


def eachfile(filepath):
    musicfile=[]
    pathdir=os.listdir(filepath)

    for s in pathdir:
        newdir = os.path.join(filepath,s) # 将文件命加入到当前文件路径后面
        if os.path.isfile(newdir):     #如果是文件
            if os.path.splitext(newdir)[1]==".csv": # 如果文件是".csv"后缀的
                musicfile.append(newdir)

    return musicfile  #返回只含txt文件的路径名

# f=eachfile(fp)


def rename_txtfilename(fp):

    f=eachfile(fp)  #利用前面的函数提取出只含txt文件的路径名，是一个list

    for i in range(len(f)):
        nowdir = os.path.split(f[i])[0] #获取文件所在文件夹的路径
        filename = os.path.split(f[i])[1] #获取文件名
        # print(nowdir+"\\\\"+filename)
        print("文件路径:%s,文件名:%s" %(nowdir,filename)) #注意print格式化输出格式
        os.rename(nowdir+"\\\\"+filename,nowdir+"\\\\"+str(i)+'.csv')

rename_txtfilename(fp)

f = os.listdir(fp) #重新列出更名后的文件列表