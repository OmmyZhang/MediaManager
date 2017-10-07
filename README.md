# MediaManager

### 在本机环境运行

配置Python环境：

```
pip install django pypinyin
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