# /get接口测试用例

from base.config_base import ConfigBase
from tool.random_test_data import faker_data


with ConfigBase(tgt_file="\\configs\\config.ini") as c_f:
    config = c_f.read_ini()
    test_path = config['api_path']['get_path']  # 接口path

def return_get_cases():
    result = []
    cases = [case_02, case_03]
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

# 测试用例01
case_01 = {
            "Casename": "api_get_01",
            "Mothed": "get",
            "Document": "get接口测试用例——提供接口依赖字段",
            "Timeout": 10,
            "Api_path": test_path,
            "Headers": {"a": faker_data(lacal="en", random_str=True),
                        "b": faker_data(lacal="en", random_str=True)},
            "Params": {"name": faker_data(lacal="en", random_str=True),
                       "age": faker_data(lacal="en", rdm_id=True)},
            "Assert": {"fields": "origin"}
         }

# 测试用例02
case_02 = {
            "Casename": "api_get_02",
            "Mothed": "get",
            "Document": "get接口测试用例——正例",
            "Timeout": 10,
            "Api_path": test_path,
            "Headers": {"a": faker_data(lacal="en", random_str=True),
                        "b": faker_data(lacal="en", random_str=True)},
            "Params": {"name": faker_data(lacal="en", random_str=True),
                       "age": faker_data(lacal="en", rdm_id=True)},
            "Assert": {"fields": "origin"}
         }
# 测试用例03
case_03 = {
            "Casename": "api_get_03",
            "Mothed": "get",
            "Document": "get接口测试用例——正例",
            "Timeout": 10,
            "Api_path": test_path,
            "Headers": {"a": faker_data(lacal="en", random_str=True),
                        "b": faker_data(lacal="en", random_str=True)},
            "Params": {"name": faker_data(lacal="en", random_str=True),
                       "age": faker_data(lacal="en", rdm_id=True)},
            "Assert": {"fields": "origin"}
         }




if __name__ == '__main__':
    res = return_get_cases()
    for i in res:
        print(i)