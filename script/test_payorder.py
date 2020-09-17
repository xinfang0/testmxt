import requests

from api.loginApi import MtxLogin
from api.orderApi import Order
from api.payOrderApi import PayOrder


class TestPayOrder:
    def setup_class(self):
        self.session = requests.Session()
        # 实例化支付接口
        self.payorder_obj = PayOrder()

    def test_payorder(self):
        # 调用成功的登录接口
        MtxLogin().login_success(self.session)
        # 调用提交订单的接口--->jump_url 数据提取 数据关联
        Order().order(self.session)
        # 请求支付接口
        resp_pay = self.payorder_obj.pay_order(self.session)
        # 断言
        assert "支付成功" in resp_pay.text
