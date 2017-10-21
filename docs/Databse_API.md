# 用户、文件、Tag相关接口

[TOC]

## API

### accouts.views

+ createUser(username,passwd,email) 返回id
  + int
+ getUser(id) 返回一个User(用法见下一部分)
  + User

### setting.views

+ createBelong(ui,gi) 令id为ui的用户属于id为gi的组(建议用前检查gi是不是一个组)，无返回值
  + 无
+ checkBelong(ui,gi) 检查ui是否属于gi
  + boolean
+ groupMems(gi) 返回id为gi的组包含的所有用户
  + int数组
+ userGroups(ui) 返回id为ui的用户属于的所有组
  + int数组

### files.views

+ createFileToTag(fi,ti) 令文件fi拥有tag ti
  + 无
+ checkFileToTag(fi,ti)
  + boolean
+ tagFiles(ti)
  + int数组
+ fileTags(fi)
  + int数组
+ getTag(id)
  + StTag
+ getFile(id)
  + StFile
+ newFile(path,name) 返回id
  + int
+ newTag(name,isGroup = False) 返回id
  + int
+ allGroup() 所有组
  + int数组



## 暴露的model

未来可能考虑进一步封装

除列举的属性外还包含一个不可修改的id

若要修改**改后请使用save()**

示例用法：

```python
uu = getUser(usr)

uu.username = "new name"
uu.save()
```

*更多用法见files/tests.py*



+ User
  + username
  + first_name
  + last_name
  + email
  + password  哈希后的值，要改密码请使用``uu.set_password("new passwd")``
+ StTag
  + name
  + isGroup
+ StFile
  + path
  + name
