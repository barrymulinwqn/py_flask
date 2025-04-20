from sqlalchemy.util.preloaded import orm


class User(object):
    # 构造方法
    def __init__(self, name):
        id = object.Column(object.Integer, primary_key=True)  # 主键
        name = object.Column(object.String(20))
        self.name = name

    @orm.reconstructor()
    def init_on_load(self):
         a = ''



