#内容介绍
本框架主要使用excel读取各种操作和被操作的元素.
添加logging模块 来确定用例优先级的报错
basepage封装各种方法
python + unnitest + xlrd + logging(待定) + configparser(读取url，账号，密码，) + HTMLtestrunner(待定)

确定页面的操作，点击（click)<元素，下选列表，复选>，输入(send_keys),清空（clear)<登录输入框，搜索框>,弹窗内容处

-svoc
-run方法      unittest测试用例，生成测试报告
--public     共有类   日志，读取config,读取excel,读取yaml方法和相关文件
--page       页面    基础selenium封装；每个页面功能，主要包括basepage,主页面，和主要功能页面；
--testCase   测试用例  引用page页面，集成unittest.TestCase,测试各功能
--report     生成测试结果报告存储路径
--screenshot 截图存放路径
--log        日志存放路径