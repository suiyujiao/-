from app.libs.redprint import RedPrint
from flask import request, jsonify, g
from app.models.address import MemberAddress
from app import db

api = RedPrint(name='address', description='订单视图')


@api.route('/add',methods=['POST'])
def add():
   res = {'code': 1, 'msg': '成功', 'data': {}}
   member = g.member
   if not member:
      res['code'] = -1
      res['msg'] = '验证失败'
      return jsonify(res)

   nickame = request.form.get('nickname')
   mobile = request.form.get('mobile')
   province_id = request.form.get('province_id')
   province_str = request.form.get('province_str')
   city_id = request.form.get('city_id')
   city_str = request.form.get('city_str')
   area_id = request.form.get('area_id')
   area_str = request.form.get('area_str')
   address = request.form.get('address')


   if not all([nickame,mobile,province_str,city_id]):
      res['code'] = -1
      res['msg'] = '参数不全'
      return jsonify(res)

   memberaddress = MemberAddress()
   memberaddress.nickname = nickame
   memberaddress.mobile = mobile
   memberaddress.province_id = province_id
   memberaddress.province_str = province_str
   memberaddress.city_id = city_id
   memberaddress.city_str = city_str
   memberaddress.area_id = area_id
   memberaddress.area_str = area_str
   memberaddress.address = address
   memberaddress.member_id = member.id

   count = MemberAddress.query.filter_by(member_id=member.id,is_default=1).count()
   if count == 0:
      memberaddress.is_default = 1
   else:
      memberaddress.is_default = 0
   db.session.add(memberaddress)
   db.session.commit()
   return jsonify(res)

@api.route('/list1')
def list1():
   res = {'code': 1, 'msg': '成功', 'data': {}}
   member = g.member
   if not member:
      res['code'] = -1
      res['msg'] = '验证失败'
      return jsonify(res)
   memberaddresses = MemberAddress.query.filter_by(member_id=member.id).all()
   addressList = []
   for address in memberaddresses:
      temp_address = {}
      temp_address['id'] = address.id
      temp_address['name'] = address.nickname
      temp_address['mobile'] = address.mobile
      temp_address['isDefault'] = address.is_default
      temp_address['detail'] = address.province_str+address.city_str+address.area_str+address.address
      addressList.append(temp_address)
   res['data']['addressList'] = addressList

   return jsonify(res)