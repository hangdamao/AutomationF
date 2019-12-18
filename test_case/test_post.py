# author = "hang"
# created 14.08.2019

from base.requests_base import RequestsBase
from base.log_base import MyLog
import pytest
from configs import post_cases

logger = MyLog("test_post")


class TestPost:

	params_list = post_cases.return_post_cases()

	@pytest.mark.parametrize("Casename, Mothed, Document, Timeout, Api_path, Headers, Params, Assert", params_list)
	def test_post(self, Casename, Mothed, Document, Timeout, Api_path, Headers, Params, Assert):
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
	pytest.main(['-s', 'test_post.py'])