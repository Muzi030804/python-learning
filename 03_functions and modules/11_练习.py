# 函数、模块和类型注解综合练习

# 定义一个函数,用于根据传入的一批商品信息(商品名,价格,数量),优惠(优惠券,积分抵扣),运费信息计算订单的总金额
# 具体规则如下:
# 优惠券需要商品金额慢5000才可以使用,且优惠券金额不能超过商品总价
# 积分抵扣需要商品总金额满5000才可以使用,100 积分抵扣1元(且抵扣金额部门超过商品总价,积分只能整百抵扣)

# def clac_order_price(goods,discount,freight):
#     goods_price = goods['价格']*goods['数量']
#     if goods_price > 5000:
#         goods_price = goods_price - discount['优惠券'] - discount['积分']//100
#     return goods_price + freight
#
# good = {"商品名":'phone','价格':2000,'数量':3}
# discount = {'优惠券':200,'积分':2000}
# print(clac_order_price(good,discount,2000))

def clac_order_price(*args: tuple[str,float,int],coupon:int =0,score:int=0,freight=0) -> float | int:
    """

    :param args: 物品信息(商品名,价格,数量)
    :param coupon: 优惠券
    :param score: 积分抵扣
    :param freight: 运费
    :return: 订单总金额
    """
    #商品金额
    total_price = [goods[1]*goods[2] for goods in args]
    total_cost = sum(total_price)

    #扣减优惠券
    if total_cost >= 5000:
        if coupon > total_cost:
            coupon = total_cost

        total_cost = total_cost - coupon

    #扣减积分抵扣
    if total_cost >= 5000:
        discount = score//100
        if score//100 > total_cost:
            discount = total_cost

        total_cost = total_cost - discount

    #添加运费
    total_cost = total_cost + freight

    return total_cost
print(clac_order_price(('phone',2000,3),('pad',1000,2),coupon=200,score=2000,freight=500))
print(clac_order_price(('phone',2000,1),('pad',1000,2),freight=100))
