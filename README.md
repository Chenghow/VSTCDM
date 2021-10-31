# VSTCDM-批量下载广东省志愿服务时间证书
    由于某种原因，学生只能通过此证书上的二维码进行志愿活动

VSTCDM即Voluntary Service Time Certificate Download Manager，志愿服务时间证书下载器，*仅支持广东省注册志愿者*

**需要python3环境与requests、pikepdf库**

使用前，请编辑**list.txt**批量下载名单文件，格式如下

    班别(文件名)+姓名+身份证号
    班别(文件名)+姓名+身份证号
    ......
各个元素以空格符相连，请严格按照格式写入

**下载错误名单将会在error_list中显示**
# 它的优势
- 轻型便捷
- 支持批量下载
- 输出下载错误名单