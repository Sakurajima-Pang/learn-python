一个通用的 manager 类通常需要以下几类方法：
类别	说明	示例
增	添加/创建资源	add(), create(), register()
删	移除/注销资源	remove(), delete(), unregister()
改	修改/更新资源	update(), modify(), set()
查	查找/获取资源	get(), find(), search(), list()
验证	检查状态或存在性	exists(), is_valid(), has()
展示	可读化输出	__str__(), __repr__(), display()
统计	计数/汇总	count(), summary()
生命周期	初始化/清理	__init__(), close(), reset()