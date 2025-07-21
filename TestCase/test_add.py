import os

from common.Logger import Log


class Test_add:

    @classmethod
    def setup_class(self):
        file = os.path.basename(__file__)
        log = Log(file)
        self.logger = log.Logger()  # ✅ 用 self 没问题
        self.logger.info("setup_class called")

    @classmethod
    def teardown_class(self):
        self.logger.info("teardown_class called")

    def test_one(self):
        self.logger.info("test_one called")
