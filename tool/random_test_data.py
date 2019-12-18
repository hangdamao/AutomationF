import random
from faker import Faker
import time

# 测试数据准备库

en_faker = Faker()  # 默认为英文数据
china_faker = Faker(locale="zh_CN")  # 中文数据
ar_faker = Faker(locale="ar")  # 阿拉伯语


def faker_data(lacal="en", name=None, phone=None, mail=None, rdm_id=None, date=None, random_str=None):
    """随机手机号码"""
    if lacal == "en":
        if name is not None:
            return en_faker.name()
        if phone is not None:
            return en_faker.phone_number()
        if mail is not None:
            return en_faker.email()
        if rdm_id is not None:
            return en_faker.random_int(min=1, max=120)
        if date is not None:
            return en_faker.date_time()
        if random_str is not None:
            return en_faker.pystr(min_chars=10, max_chars=100)
    if lacal == "zh_CN":
        if name is not None:
            return china_faker.name()
        if phone is not None:
            return china_faker.phone_number()
        if mail is not None:
            return china_faker.email()
        if rdm_id is not None:
            return china_faker.random_int(min=100000, max=9999999)
        if date is not None:
            return china_faker.date_time()
        if random_str is not None:
            return china_faker.pystr(min_chars=10, max_chars=100)
    if lacal == "ar":
        if name is not None:
            return ar_faker.name()
        if phone is not None:
            return ar_faker.phone_number()
        if mail is not None:
            return ar_faker.email()
        if rdm_id is not None:
            return ar_faker.random_int(min=100000, max=9999999)
        if date is not None:
            return ar_faker.date_time()
        if random_str is not None:
            return ar_faker.pystr(min_chars=10, max_chars=100)


def faker_order_num(min_s, max_s):
    '''生成订单号'''
    return en_faker.pystr(min_chars=min_s, max_chars=max_s)


def random_order_no():
    """获取随机的的订单二维码"""
    return ''.join(random.sample("hjjkdzaMjffhsiGRGfdaRe", 8))


def format_get_now_time():
    """获取当前时间，并格式化输出"""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def random_local_phone(lacal):
    """产生指定的阿拉伯地区的号码"""
    if lacal == "Saudi_Arabie":  # 沙特阿拉伯
        return str(en_faker.random_int(min=500000000, max=599999999))  # 以5开头，长度为9
    if lacal == "United_Arab_Emirates":  # 阿拉伯联合酋长国
        return str(en_faker.random_int(min=500000000, max=599999999))  # 以5开头，长度为9
    if lacal == "Qutar":  # 卡特尔
        res_list = []
        res_1 = en_faker.random_int(min=30000000, max=39999999)  # 以3开头，长度为8
        res_list.append(res_1)
        res_2 = en_faker.random_int(min=40000000, max=49999999)  # 以4开头，长度为8
        res_list.append(res_2)
        res_3 = en_faker.random_int(min=50000000, max=59999999)  # 以5开头，长度为8
        res_list.append(res_3)
        res_4 = en_faker.random_int(min=60000000, max=69999999)  # 以6开头，长度为8
        res_list.append(res_4)
        res_5 = en_faker.random_int(min=70000000, max=79999999)  # 以7开头，长度为8
        res_list.append(res_5)
        return str(random.sample(res_list, 1)[0])
    if lacal == "Kuwait":  # 科威特
        res_list = []
        res_1 = en_faker.random_int(min=50000000, max=59999999)  # 以5开头，长度为8
        res_list.append(res_1)
        res_2 = en_faker.random_int(min=60000000, max=69999999)  # 以6开头，长度为8
        res_list.append(res_2)
        res_3 = en_faker.random_int(min=90000000, max=99999999)  # 以9开头，长度为8
        res_list.append(res_3)
        return str(random.sample(res_list, 1)[0])
    if lacal == "Bahrain":  # 巴林
        res_list = []
        res_1 = en_faker.random_int(min=30000000, max=39999999)  # 以3开头，长度为8
        res_list.append(res_1)
        res_2 = en_faker.random_int(min=60000000, max=69999999)  # 以6开头，长度为8
        res_list.append(res_2)
        return str(random.sample(res_list, 1)[0])
    if lacal == "Oman":  # 阿曼
        res_list = []
        res_1 = en_faker.random_int(min=70000000, max=79999999)  # 以7开头，长度为8
        res_list.append(res_1)
        res_2 = en_faker.random_int(min=90000000, max=99999999)  # 以9开头，长度为8
        res_list.append(res_2)
        return str(random.sample(res_list, 1)[0])
    if lacal == "Iraq":  # 伊拉克
        return str(en_faker.random_int(min=7000000000, max=7999999999))  # 以7开头，长度为10


if __name__ == "__main__":
    # name
    print("------------name------------")
    res = faker_data(lacal="en", name=1)
    print(res)
    res = faker_data(lacal="zh_CN", name=1)
    print(res)
    res = faker_data(lacal="ar", name=1)
    print(res)
    # phone
    print("-------------phone-----------")
    res = faker_data(lacal="en", phone=1)
    print(res)
    res = faker_data(lacal="zh_CN", phone=1)
    print(res)
    res = faker_data(lacal="ar", phone=1)
    print(res)
    # mail
    print("-----------mail-------------")
    res = faker_data(lacal="en", mail=1)
    print(res)
    res = faker_data(lacal="zh_CN", mail=1)
    print(res)
    res = faker_data(lacal="ar", mail=1)
    print(res)
    # rdm_id
    print("----------rdm_id--------------")
    res = faker_data(lacal="en", rdm_id=1)
    print(res)
    res = faker_data(lacal="zh_CN", rdm_id=1)
    print(res)
    res = faker_data(lacal="ar", rdm_id=1)
    print(res)
    # date
    print("------------date------------")
    res = faker_data(lacal="en", date=1)
    print(res)
    res = faker_data(lacal="zh_CN", date=1)
    print(res)
    res = faker_data(lacal="ar", date=1)
    print(res)
    # random_str
    print("------------random_str------------")
    res = faker_data(lacal="en", random_str=1)
    print(res)
    res = faker_data(lacal="zh_CN", random_str=1)
    print(res)
    res = faker_data(lacal="ar", random_str=1)
    print(res)

    print()

    print("------------+966------------")
    res = random_local_phone(lacal="Saudi_Arabie")
    print(res)
    print(type(res))
    print("------------+971------------")
    res = random_local_phone(lacal="United_Arab_Emirates")
    print(res)
    print(type(res))
    print("------------+974------------")
    res = random_local_phone(lacal="Qutar")
    print(res)
    print(type(res))
    print("------------+965------------")
    res = random_local_phone(lacal="Kuwait")
    print(res)
    print(type(res))
    print("------------+973------------")
    res = random_local_phone(lacal="Bahrain")
    print(res)
    print(type(res))
    print("------------+968------------")
    res = random_local_phone(lacal="Oman")
    print(res)
    print(type(res))
    print("------------+964------------")
    res = random_local_phone(lacal="Iraq")
    print(res)
    print(type(res))

    print()

    res = faker_order_num(min_s=8, max_s=8)
    print(res)