# djangoProject
工欲善其事，必先利其器

1.python环境
新款的MAC笔记本(M1芯片)，MAC自带了python2，我们要安装python3，python2和python3并存。
MAC M1系统只支持python 3.9!!!

安装git---安装Homebrew---安装python3

2.PyCharm创建Django项目
建议用虚拟环境

3.利用rbac实现权限管理
注意settings中DEBUG模式要开启，否则会出现admin管理界面样式丢失
jquery-3.2.1.js文件作参考用

4.执行Django命令
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

5.玩转rbac权限
RBAC（Role-Based Access Control，基于角色的访问控制），就是用户通过角色与权限进行关联
所以先去配置吧http://127.0.0.1:8000/rbac/
