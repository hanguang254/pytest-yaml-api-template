import os

from common.Logger import Log


class Test_add:

    def setup_method(self, method):
        class_name = self.__class__.__name__        # Test_add
        method_name = method.__name__               # test_one
        file = os.path.basename(__file__)
        log = Log(file, suffix=f"{class_name}_{method_name}")
        self.logger = log.Logger()
        self.logger.info(f"开始执行用例：{class_name}.{method_name}")

    def teardown_method(self, method):
        self.logger.info("用例执行结束")

    def test_one(self):
        self.logger.info("这是 test_one 的日志")

    def test_two(self):
        self.logger.info("这是 test_two 的日志")
