本应用将提供用于文件，文件夹操作的各种接口，所有的接口位于views.py中，其他函数都用于完成内部的逻辑实现，外部不用关心
文件接口如下：
（1）Upload_file：
Input:
No.1 ————> 待上传的文件（request.FILES.get的返回类型）
No.2 ————> 要存储的路径（e.g. data/weijy/1.pptx)
Output:
True ————> 上传成功
False ————> 存储路径不存在或硬盘写满，上传失败

（2）Download_file:
Input:
No.1 ————> 下载路径（e.g. data/weijy/1.pptx）
Output:
一个获取http_response的文件数据流生成器，可以直接通过该生成器来构造StreamingHttpResponse

(3) Remove:
Input:
No.1 ————> 文件／目录路径（e.g: data/weijy/1.pptx）
Output:
True ————> 删除成功
False ————> 文件或路径不存在，删除失败

(4) RM(实现了重命名和移动双重功能）:
Input:
No.1 ————> 文件／目录路径（e.g: 重命名：data/weijy/1.pptx 移动：data/weijy/1.pptx）
No.2 ————> 新路径（e.g: 重命名：data/weijy/2.pptx 移动:data/weijy1/1.pptx）
Output:
True ————> 重命名／移动成功
False ————> 文件或路径不存在，重命名／移动失败

(5) New(新建文件夹):
Input:
No.1 ————> 新建路径（e.g：data/weijy）
No.2 ————> 新建文件夹名称（默认名称：New_Folder）
Output:
True ————> 新建文件夹成功
False ————> 路径不存在，新建失败


