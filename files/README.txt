本应用将提供用于文件，文件夹操作的各种接口，所有的接口位于views.py中，其他函数都用于完成内部的逻辑实现，外部不用关心
文件接口如下：
（1）Upload_file：
Input:
No.1: post_name 上传文件时Http标签input中对应的name		
No.2: 上传文件的Http请求
No.3: 用户名
No.4: 用户的操作路径（eg:data/weijy15/test/file/oo）
Output:
Result: 一个指示上传结果的字符串（有两种可能"Success","Fail"）

（2）Download_file:
Input:
No.1: 文件详细路径
Output:
Result:
如果下载成功 返回Http_response
如果失败将返回串“Fail”
