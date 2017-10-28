本应用将提供用于文件，文件夹操作的各种接口，所有的接口位于views.py中，其他函数都用于完成内部的逻辑实现，外部不用关心
文件接口如下：
按上一次会议的讨论结果，上传文件和移动功能类似，下载文件则需要另外实现，在这里不提供相应的接口
(3) remove(删除文件或文件夹):
调用形式：Remove(path)
Input:
No.1 ————> 文件／目录路径（e.g: data/weijy/1.pptx）
Output:
True ————> 删除成功
False ————> 文件或路径不存在，删除失败

(4) rm(实现了重命名和移动双重功能）:
调用模式: Remove(old_path,new_path)
Input:
No.1 ————> 文件／目录路径（e.g: 重命名：data/weijy/1.pptx 移动：data/weijy/1.pptx）
No.2 ————> 新路径（e.g: 重命名：data/weijy/2.pptx 移动:data/weijy1/1.pptx）
Output:
True ————> 重命名／移动成功
False ————> 文件或路径不存在，重命名／移动失败

(5) new(新建文件夹):
调用形式：New(path, new_folder_name)
Input:
No.1 ————> 新建路径（e.g：data/weijy）
No.2 ————> 新建文件夹名称（默认名称：New_Folder）
Output:
True ————> 新建文件夹成功
False ————> 路径不存在，新建失败

(6) list(获取文件的详细信息):
调用形式：List(path)
No.1 ————> 输入文件的路径
输出格式一个包含当前路径下所有文件和文件夹的list 
