# author == "hang"

from collections import ChainMap


class FormatAPIResponse(object):
    def __init__(self):
        self.__res_list = []

    def is_result(self, data):
        # 判断能不能对目标进行字典对象转账，能返回Ture， 不能返回False
        try:
            res = eval(data)
            if isinstance(res, int) or isinstance(res, float):
                return None
        except Exception:
            return None
        return res

    def format_main(self, obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if self.is_result(v) is None:
                    if isinstance(v, list) or isinstance(v, tuple):
                        return self.format_main(v)
                    else:
                        self.__res_list.append({k: v})
                else:
                    return self.format_main(v)
        if isinstance(obj, list) or isinstance(obj, tuple):
            for i in obj:
                return self.format_main(i)
        if isinstance(obj, str):
            r = self.is_result(obj)
            return self.format_main(r)

    def return_chainmap_obj(self):
        # print(len(self.__res_list))
        res = ChainMap(*self.__res_list)
        return res


def get_target_value(obj, *target_key):
    f = FormatAPIResponse()
    f.format_main(obj)
    res = f.return_chainmap_obj()
    print(f"合并整理返回结果：\n{res}")
    if len(target_key) == 1:
        return res.get(*target_key)
    if len(target_key) <= 0:
        print("请给出你想要目标key!")
    if len(target_key) >= 2:
        result = []
        for i in target_key:
            result.append(res.get(i))
        return result


if __name__ == '__main__':
    # obj = {
    #     "code":
    #     0,
    #     "message":
    #     '{"paymentToken":"ebea9bd1cf6b447baf741ca0e9eb12d6","cardList":[{"cardId":"9901084493003403225","cardType":"0","cardBrandName":"Account Balance","tailNum":"3225","balance":"29960300","bankImg":"","minorCurrency":"CNY","minorAmount":"700","minorDecimalPlace":"2","mainAmount":"100","mainCurrency":"USD","mainDecimalPlace":"2","usdAmount":"100","balanceFlag":"0","maxAmount":"","mixAmount":"","logoImg":"http://gw.legion.zcsmart.com.cn/img/3f23af086f7e990eac3cfd96bcccb01f","chanId":"","tips":""},{"cardId":"","cardType":"2","cardBrandName":"Credit Cards","tailNum":"","balance":"","bankImg":"","minorCurrency":"USD","minorAmount":"100","minorDecimalPlace":"2","mainAmount":"377.000","mainCurrency":"BHD","mainDecimalPlace":"3","usdAmount":"100","balanceFlag":"0","maxAmount":"","mixAmount":"","logoImg":"http://gw.legion.zcsmart.com.cn/img/f6be690ab1577fa6dd03c16391d2b87a","chanId":"2","tips":"Please complete the transaction within 1 hour"}]}'
    # }
    # res = get_target_value(obj, "paymentToken", "cardId")
    # print(res)


    obj = {'code': 0,
           'message': '{"paymentToken":"07915e017a0c4d98a5b4f359f3136dfa","merName":"WPay MALL","cardList":[{"minorCurrency":"CNY","minorAmount":"700.00","minorDecimalPlace":"2","usdAmount":"100","mainAmount":"100","mainCurrency":"USD","mainDecimalPlace":"2","cardType":"0","cardBrandName":"Account Balance","balanceFlag":"0","maxAmount":"","mixAmount":"","paymentList":[{"payId":"0000001600","payName":"金额联机","currAvailAt":"100049821999","prdtTitle":"金额联机","prdtNo":"1600","sttlUnit":"2","payAmt":100,"exchAmt":100,"perUnit":"0","alpCode":"","numCode":""}],"rebate":"","cardId":"9901084493003403225","tailNum":"3225","localAmount":"700.00","balance":"100049821999","logoImg":"http://gw.legion.zcsmart.com.cn/img/3f23af086f7e990eac3cfd96bcccb01f","chanId":"","tips":"","mainPrdtNo":""},{"minorCurrency":"USD","minorAmount":"100","minorDecimalPlace":"2","usdAmount":"100","mainAmount":"377.000","mainCurrency":"BHD","mainDecimalPlace":"3","cardType":"2","cardBrandName":"Credit Cards","balanceFlag":"0","maxAmount":"","mixAmount":"","paymentList":[],"rebate":"","cardId":"","tailNum":"","localAmount":"","balance":"","logoImg":"http://gw.legion.zcsmart.com.cn/img/f6be690ab1577fa6dd03c16391d2b87a","chanId":"2","tips":"Please complete the transaction within 1 hour","mainPrdtNo":""}]}'}
    f = FormatAPIResponse()
    f.format_main(obj)
    res = f.return_chainmap_obj()
    print(res)

    res = get_target_value(obj, 'merName')
    print(res)

