# exam

## django+vue 上传 TXT 的软考试题 加载成页面

## 目的

将 TXT 版本的软考试题转换成页面，可以进行选项选择，查看答案及解析，方便使用

## 功能点

第一次使用 django 模板加 vue，故记录一下基础知识

1、搭建 python3 环境
2、执行 pip install django=2.2 # 带版本安装 django

```
 执行pip install django=2.2时经常报错，可以去django官网下载安装包，本地执行 pip install 安装包地址 安装
```

3、创建项目

```
django-admin.py startproject 项目名称

```

目录说明：

项目名称: 项目的容器。
manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
项目名称/**init**.py: 一个空文件，告诉 Python 该目录是一个 Python 包。
项目名称/settings.py: 该 Django 项目的设置/配置。
项目名称/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
项目名称/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。

4、在 项目名称 目录底下创建 templates 目录并建立 hello.html 文件

5、项目名称/settings.py，修改 TEMPLATES 中的 DIRS 为 [BASE_DIR+"/templates",]

6、pip install mysqlclient 安装 mysql 配置

在项目的 settings.py 文件中找到 DATABASES 配置项，将其信息修改为：

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 或者使用 mysql.connector.django
        'NAME': 'test',
        'USER': 'test',
        'PASSWORD': 'test123',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```

7、Django 规定，如果要使用模型，必须要创建一个 app。我们使用以下命令创建一个 app_1 的 app:

```
django-admin startapp app_1
```

8、接下来在 settings.py 中找到 INSTALLED_APPS 这一项，如下

```
INSTALLED_APPS = (
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'app_1', # 添加此项
)

$ python manage.py migrate   # 创建表结构

$ python manage.py makemigrations app_1  # 让 Django 知道我们在我们的模型有一些变更
$ python manage.py migrate app_1   # 创建表结构
```

9、引入 vue 将 vue 标签包裹在以下代码中

 <!--vue 绑定和Django的jinja2模板系统使用的标签是一样的，为了区分我们需要用verbatim将vue的标签包围起来-->

    {% verbatim myblock %}
    ...
    {% endverbatim myblock %}

```
# 更新数据库
python manage.py makemigrations

python manage.py migrate

# 运行
python manage.py runserver 0.0.0.0:8000

```
