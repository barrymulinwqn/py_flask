# py_flask
## flask learning

1. .flaskenv 用来存储 Flask 命令行系统相关的公开环境变量
2. 而 .env 则用来存储敏感数据 **不提交到repo中，请自行在本地创建**

## 如何运行
按照惯例，我们把程序保存为 app.py，确保当前目录是项目的根目录，并且激活了虚拟环境，然后在命令行窗口执行 flask run 命令启动程序（按下 Control + C 可以退出）

1. 当用户在浏览器地址栏访问这个地址，在这里即 http://localhost:5000/
2. 服务器解析请求，发现请求 URL 匹配的 URL 规则是 /，因此调用对应的处理函数 hello()
3. 获取 hello() 函数的返回值，处理后返回给客户端（浏览器）
4. 浏览器接受响应，将其显示在窗口上


## 部署前的准备
首先，我们需要生成一个依赖列表，方便在部署环境里安装。使用下面的命令把当前依赖列表写到一个 requirements.txt 文件里：
> (env) $ pip freeze > requirements.txt


## 创建数据库表
- 模型类创建后，还不能对数据库进行操作，因为我们还没有创建表和数据库文件。下面在 Python Shell 中创建了它们
  > (env) $ flask shell
  >
    > from app import db
    > 
    >  db.create_all()
    
- 打开文件管理器，你会发现项目根目录下出现了新创建的数据库文件 data.db。这个文件不需要提交到 Git 仓库，我们在 .gitignore 文件最后添加一行新规则：  
    > *.db
- 如果你改动了模型类，想重新生成表模式，那么需要先使用 db.drop_all() 删除表，然后重新创建：
    > db.drop_all()
    > 
    > db.create_all()
    > 
- 注意这会一并删除所有数据，如果你想在不破坏数据库内的数据的前提下变更表的结构，需要使用数据库迁移工具，比如集成了 Alembic 的 Flask-Migrate 扩展。