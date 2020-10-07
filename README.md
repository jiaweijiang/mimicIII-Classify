# 项目总览

**project:** *patients classify based on MIMIC III*
<br />
**platform:** *ubuntu/macos*
<br />
**author:** *jiawei.jiang*
<br />
**date:** *2020.10.07*
<br />
**format:** *markdown*

## 文件及作用
- common\_fun.py *eg. 执行`python common_fun.py`*
    - 创建需要的文件夹
    - 定义在其他文件中使用的共同函数
- database\_wrapper.py
    - 数据库连接信息
    - 定义所有的数据库查询动作
- data\_process\_handler.py
    - 定义数据处理函数
- data\_process\_main.py
    - 定义数据处理流程，只关心逻辑，具体的数据处理方法在 data_process_handler.py
- data\_stas\_handler.py
    - 定义数据统计函数
- data\_stats\_main.py
    - 定义数据统计流程，只关心逻辑，具体的统计方法在 data_stac_handler.py
- main.py
    - 定义整体的逻辑顺序
- test.py
    - 测试用文件

## 备注
- data_process 基本上写完了
- data_stas 未写完
- main 未写完