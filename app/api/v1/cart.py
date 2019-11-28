from app.libs.redprint import RedPrint
from flask import request,jsonify,g
from app import db
from app.models.member import Member
from app.models.food import Food
from app.models.cart import MemberCart
from app.utils.common import buildPicUrl
from app.service.memberService import memberService
api = RedPrint('cart',description='购物车模块')
@api.route('/add',methods=['POST','GET'])
def add():
    res = {'code': 1, 'msg': '成功', 'data': {}}
    # try:
    #     token = request.headers.get('token')
    #
    #     if not token:
    #         res['code'] = -1
    #         res['msg'] = '必须登录'
    #         return jsonify(res)
    #     tuple_token = token.split('#')
    #
    #     if len(tuple_token) != 2:
    #         res['code'] = -1
    #         res['msg'] = 'token错误'
    #         return jsonify(res)
    #     member = Member.query.get(tuple_token[1])
    #
    #     if not member:
    #         res['code'] = -1
    #         res['msg'] = '该用户不存在'
    #         return jsonify(res)
    #     c_token = memberService.geneAuthCode(member)
    #
    #     if c_token != tuple_token[0]:
    #         res['code'] = -1
    #         res['msg'] = 'token错误'
    #         return jsonify(res)
    member = g.member
    if not member:
        res['code'] = -1
        res['msg'] = '该用户不存在'
        return jsonify(res)
    id = request.form.get('id')
    num = request.form.get('num')
    type = request.form.get('type')

    if not all([id,num]):
        res['code'] = -1
        res['msg'] = '缺少参数'
        return jsonify(res)
    id = int(id)
    num = int(num)
    type = int(type)
    if id <= 0 :
        res['code'] = -1
        res['msg'] = 'id错误'
        return jsonify(res)
    if type == 0:
        if num <= 0:
            res['code'] = -1
            res['msg'] = '参数错误'
            return jsonify(res)
    else:
        if num != 1 and num != -1:
            res['code'] = -1
            res['msg'] = '参数错误'
            return jsonify(res)
    food = Food.query.get(id)
    if not food:
        res['code'] = -1
        res['msg'] = '食品不存在'
        return jsonify(res)
    if food.status != 1:
        res['code'] = -1
        res['msg'] = '食品已下架'
        return jsonify(res)
    if num > food.stock:
        res['code'] = -1
        res['msg'] = '库存不足'
        return jsonify(res)
    membercart = MemberCart.query.filter_by(member_id=member.id,food_id=id).first()
    if not membercart:
        membercart = MemberCart()
        membercart.food_id = id
        membercart.member_id = member.id
        membercart.quantity = num
        db.session.add(membercart)
        db.session.commit()
    else:
        membercart.quantity = membercart.quantity + num
        db.session.add(membercart)
        db.session.commit()
        return jsonify(res)
    #     if num == -1:
    #         if membercart.quantity > 1:
    #             membercart.quantity = membercart.quantity + num
    #         else:
    #             res['code'] = -1
    #             res['msg'] = '商品数量必须大于1'
    #             return jsonify(res)
    #     if membercart.quantity > food.stock:
    #         res['code'] = -1
    #         res['msg'] = '库存不足'
    #         return jsonify(res)
    #     else:
    #         db.session.add(membercart)
    #         db.session.commit()
    # res['msg'] = '添加成功'
    # return jsonify(res)

# except Exception as e:
#     res['code'] = -1
#     res['msg'] = '参数错误'
#     return jsonify(res)

@api.route('/list')
def list():
    res = {'code': 1, 'msg': '成功', 'data': {}}
    member = g.member
    if not member:
        res['code'] = -1
        res['msg'] = '该用户不存在'
        return jsonify(res)
    membercarts = MemberCart.query.filter_by(member_id=member.id).all()
    list = []
    totalPrice = 0
    for mc in membercarts:
        temp_data = {}
        food = Food.query.get(mc.food_id)
        if not food or food.status != 1:
            continue
        temp_data['id'] = mc.id
        temp_data['food_id'] = mc.food_id
        temp_data['pic_url'] = buildPicUrl(food.main_image)
        temp_data['name'] = food.name
        temp_data['price'] = str(food.price)
        temp_data['active'] = 'true'
        temp_data['number'] = mc.quantity
        totalPrice += mc.quantity * food.price
        list.append(temp_data)
    res['data']['list']=list
    res['data']['totalPrice'] = str(totalPrice)
    return jsonify(res)
import json
@api.route('/delete',methods=['POST'])
def delete():
    res = {'code': 1, 'msg': '成功', 'data': {}}
    member = g.member
    if not member:
        res['code'] = -1
        res['msg'] = '验证失败'
        return jsonify(res)
    ids = request.form.get('ids')

    if not ids:
        res['code'] = -1
        res['msg'] = '参数有误'
        return jsonify(res)
    ids = json.loads(ids)
    for id in ids:
        membercart = MemberCart.query.get(id)
        if not membercart:
            continue
        db.session.delete(membercart)
        db.session.commit()

    return jsonify(res)









