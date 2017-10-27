# 用户、文件、Tag相关接口

[TOC]

## API

### accouts.views

+ create\_user(username,passwd,email) 返回id
  + int
+ get\_user(id) 返回一个User(用法见下一部分)
  + User

### setting.views

+ create\_Belong(ui,gi) 令id为ui的用户属于id为gi的组(建议用前检查gi是不是一个组)，无返回值
  + 无
+ check\_Belong(ui,gi) 检查ui是否属于gi
  + boolean
+ group\_mems(gi) 返回id为gi的组包含的所有用户
  + int数组
+ user\_groups(ui) 返回id为ui的用户属于的所有组
  + int数组

### files.views

+ create\_fileToTag(fi,ti) 令文件fi拥有tag ti
  + 无
+ check\_FileToTag(fi,ti)
  + boolean
+ tag\_files(ti)
  + int数组
+ file\_tags(fi)
  + int数组
+ get\_tag(id)
  + StTag
+ get\_file(id)
  + StFile
+ new\_file(path,name) 返回id
  + int
+ new\_tag(name,isGroup = False) 返回id
  + int
+ all\_group() 所有组
  + int数组
+ files\_here(owner, path) 某一用户在某一位置的所有文件
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
  + first\_name
  + last\_name
  + email
  + password  哈希后的值，要改密码请使用``uu.set_password("new passwd")``
+ StTag
  + name
  + isGroup
+ StFile
  + path
  + name
