# MediaManager

## 开发说明

### API文档

位于`docs/swagger.yml`

`swagger`是一种通用的WebAPI描述格式。可自动生成前后端的代码（可惜并没有`Django-Rest-Framework`）

打开在线编辑器 https://editor.swagger.io/

把全文复制到左侧编辑器中，在右侧查看

### 后端单元测试

写在各APP文件夹下的`tests.py`文件中。

如果要分多个文件，则需移除`tests.py`文件，新建`tests`文件夹，在其中新建若干`test_*.py`文件。具体写法见样例：`home/tests/test_sample.py`。

注意：方法必须以`test`开头才可以被识别为测例。

### RESTful API

使用框架：`Django-Rest-Framework`

官网：http://www.django-rest-framework.org

已经创建了一个官网样例，在`sampleApi`文件夹下。

可以访问：http://127.0.0.1:8000/api/ 感受一下。

### 前后端分离

#### 整体思想

禁用后端模板渲染，改用上述RESTful框架提供WebAPI。后端接受HTTP请求，返回JSON格式的纯文本。

前端每次获取纯HTML页面，由嵌入的JavaScript去调用后端API，然后渲染到页面中，必要时执行页面跳转。

同时前端的页面和逻辑也可以分离，HTML和JS分别由两个人写，只需约定好HTML元素的id即可。

#### 这样做有如下好处

* 前后端完全解耦，只需约定好API格式，后端不关心HTML，前端不关心Python。
* 便于两边的测试。后端只需测试WebAPI，即模拟HTTP请求，检查返回值是否正确。前端可以自己构造数据查看页面效果。

#### 一个样例如下

首先访问首页登陆admin用户（否则接下来会无权访问）

然后访问：http://127.0.0.1:8000/static/users/index.html

#### 项目结构

前端完全位于`static`文件夹中，按实际URL组织层次，访问时不经过Python转发

后端分布于各个app文件夹中，不含HTML模板

## 部署运行

### 在本机环境运行

使用Python2.7

配置Python环境：

```
pip install -r requirements.txt 
```

启动：

```
python manage.py runserver
```

访问：http://localhost:8000

初始用户名：admin，密码：ruan_gong

### 用Docker部署运行

Build Docker：
```
docker build -t mediamanager .
```

Run Docker:
```
docker run -p 8000:8000 --name=mediamanager -d mediamanager
```
