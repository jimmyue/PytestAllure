pytest  https://docs.pytest.org/en/latest/ 

allure  https://docs.qameta.io/allure/#_pytest


一.安装python库

pip install pytest

pip install allure-pytest

pip install allure-python-commons


二.下载allure-commandline 解压并添加环境变量，执行allure --version查看是否配置成功

https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/


三.终端执行指令生成结果,pytest会在目录下自动找test开头的py文件

pytest --alluredir={result_path}


四.生成server测试报告

allure serve {result_path}


五.生成html测试报告，据说只有火狐浏览器能打开，目前发现也打不开。。

allure generate {result_path}                  #默认路径allure-report

allure generate {result_path} --clean          #更新报告allure-report

allure generate {result_path} -o {html_path}   #生成到指定路径{html_path}


六.jenkins设置

1.插件安装Allure Jenkins Plugin

2.Manage Jenkins -> Global Tool Configuration，设置jdk和Allure Commandline


七.新建jenkins+pytest+allure项目

1.构建：Execute Windows batch command

D:
cd D:\github\PytestAllure
call pytest --alluredir %workspace%\allure_result
exit 0

2.构建后操作：allure report

Result Path: allure_result
Properties key: allure.tests.management.pattern
Properties value: http://tms.company.com/%s
Jdk : dk1.8.0_221(选择自己设置的)
Report path: allure-report


八.生成的Allure报告中，左侧菜单栏最下方可以切换显示语言

