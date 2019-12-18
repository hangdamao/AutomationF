# author = "hang"
# created 11.12.2019

from base.requests_base import RequestsBase
from base.log_base import MyLog
import pytest
from configs import get_cases
from base.redis_base import RedisBase

logger = MyLog("test_get")


class TestGet:

	params_list = get_cases.return_get_cases()

	def test_get_general(self):
		case_01 = get_cases.case_01
		with RequestsBase(case_name=case_01.get('Casename'),
						  run_mothed=case_01.get('Mothed'),
						  api_path=case_01.get('Api_path'),
						  time_out=case_01.get('Timeout'),
						  headers=case_01.get('Headers'),
						  params=case_01.get('Params'),
						  document=case_01.get('Document')) as requester:
			res = requester.requests_run()
			assert isinstance(res, dict)
			assert case_01.get('Assert').get("fields") in res
			with RedisBase() as red:
				red.redis_set(key="age", value=res.get('args').get('age'))
				red.redis_set(key="name", value=res.get('args').get('name'))
			logger.info(f">>>>>>>>>>>>>>>>>>>用例：{case_01.get('Casename')}, 测试完毕<<<<<<<<<<<<<<<<<<<")

	@pytest.mark.parametrize("Casename, Mothed, Document, Timeout, Api_path, Headers, Params, Assert", params_list)
	def test_get(self, Casename, Mothed, Document, Timeout, Api_path, Headers, Params, Assert):
		with RequestsBase(case_name=Casename,
						  run_mothed=Mothed,
						  api_path=Api_path,
						  time_out=Timeout,
						  headers=Headers,
						  params=Params,
						  document=Document) as requester:
			res = requester.requests_run()
			assert isinstance(res, dict)
			assert Assert.get("fields") in res
			logger.info(f">>>>>>>>>>>>>>>>>>>用例：{Casename}, 测试完毕<<<<<<<<<<<<<<<<<<<")


if __name__ == '__main__':
	pytest.main(['-s', 'test_get.py'])