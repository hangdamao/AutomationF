# /post接口测试用例

from base.config_base import ConfigBase
from base.redis_base import RedisBase
from tool.random_test_data import faker_data


with ConfigBase(tgt_file="\\configs\\config.ini") as c_f:
    config = c_f.read_ini()
    test_path = config['api_path']['post_path']  # 接口path

with RedisBase() as red:
    age = red.redis_get(key="age")
    name = red.redis_get(key="name")

def return_post_cases():
    result = []
    cases = [case_01, case_02, case_03]
    for i in cases:
        inner_list = []
        values_Casename = i.get("Casename")
        inner_list.append(values_Casename)
        values_Mothed = i.get("Mothed")
        inner_list.append(values_Mothed)
        values_Document = i.get("Document")
        inner_list.append(values_Document)
        values_Timeout = i.get("Timeout")
        inner_list.append(values_Timeout)
        values_Api_path = i.get("Api_path")
        inner_list.append(values_Api_path)
        values_Headers = i.get("Headers")
        inner_list.append(values_Headers)
        values_Params = i.get("Params")
        inner_list.append(values_Params)
        values_Assert = i.get("Assert")
        inner_list.append(values_Assert)
        result.append(inner_list)
    return result

# 测试用例1
case_01 = {
            "Casename": "api_post_01",
            "Mothed": "post",
            "Document": "post接口测试用例——正例",
            "Timeout": 10,
            "Api_path": test_path,
            "Headers": {"Content-Type": "application/json"},
            "Params": {"name": faker_data(lacal="en", random_str=True),
                       "age": faker_data(lacal="en", rdm_id=True),
                       "male": faker_data(lacal="en", random_str=True)},
            "Assert": {"fields": "origin"}
         }

case_02 = {
            "Casename": "api_post_02",
            "Mothed": "post",
            "Document": "post接口测试用例——正例",
            "Timeout": 10,
            "Api_path": test_path,
            "Headers": {"Content-Type": "application/json"},
            "Params": {"导演/演员/时间/...": "导演:彼得·杰克逊 Peter Jackson   主演:伊利亚·伍德 Elijah Wood / 西恩... / 美国 新西兰 / 剧情 动作 奇幻 冒险",
                       "影评": "9.0 328420人评价",
                       "电影名称": "指环王2：双塔奇兵",
                       "电影封面": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p909265336.jpg",
                       "电影总结": "承前启后的史诗篇章",
                       "电影详情页": "https://movie.douban.com/subject/1291572/"},
            "Assert": {"fields": "origin"}
         }

case_03 = {
            "Casename": "api_post_03",
            "Mothed": "post",
            "Document": "post接口测试用例——获取get接口返回的数据作为参数",
            "Timeout": 10,
            "Api_path": test_path,
            "Headers": {"Content-Type": "application/json"},
            "Params": {"name": name, "age": age},
            "Assert": {"fields": "origin"}
         }


if __name__ == '__main__':
    res = return_post_cases()
    for i in res:
        print(i)