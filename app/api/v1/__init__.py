from flask import Blueprint
from . import user,member,food,cart,order,address,comment,order_shop


def createBluePrint():
    bp = Blueprint('v1', __name__)
    user.api.register(bp)
    member.api.register(bp)
    food.api.register(bp)
    cart.api.register(bp)
    order.api.register(bp)
    address.api.register(bp)
    comment.api.register(bp)
    order_shop.api.register(bp)
    return bp
