//获取应用实例
var app = getApp();

Page({
    data: {
        ids :[],
        address_id: 0,
        note:'',
        num:0,
        id:0,
        type:'0',
        // goods_list: [
        //     {
        //         id:22,
        //         name: "小鸡炖蘑菇",
        //         price: "85.00",
        //         pic_url: "/images/food.jpg",
        //         number: 1,
        //     },
        //     {
        //         id:22,
        //         name: "小鸡炖蘑菇",
        //         price: "85.00",
        //         pic_url: "/images/food.jpg",
        //         number: 1,
        //     }
        // ],
        // default_address: {
        //     name: "编程浪子",
        //     mobile: "12345678901",
        //     detail: "上海市浦东新区XX",
        // },
        // yun_price: "1.00",
        // pay_price: "85.00",
        // total_price: "86.00",
        // params: null
    },
    onShow: function () {
        var that = this;
    },
    onLoad: function (e) {
        var that = this;
        // var type = e.type;
        // if (type == '0'){
        //     that.setData({
        //     ids:JSON.parse(e.ids)
        // });
        // that.getOrderIndex()
        // }else{
        //     var id = e.id;
        //     console.log(e)
        //     var num = e.num;
        //     that.setData({
        //         id:id,
        //         num:num,
        //     });
        //     that.getOrderInfo()
        // }
        //为了区分从哪来的
        that.setData({
            type: e.type
        })
        //从立即购买
        if (that.data.type == 1) {
            that.setData({
                num: e.num
            })
        }
        //不管从购物车还是从立即购买
        that.setData({
            ids: JSON.parse(e.ids),
        })
        that.getOrderIndex()
    },
    getInput:function(e){
        this.setData({
            note:e.detail.value
        })
    },
    createOrder: function (e) {
        var that = this;

        if (that.data.type == 0) {
            var url = app.buildUrl('/v1/order_shop/create')
            var data =  {
                'ids': JSON.stringify(that.data.ids),//商品ids
                'address_id': that.data.address_id,
                'note': that.data.note
            }
        }else{
            var url = app.buildUrl('/v1/order_shop/create1')
            var data =  {
                'ids': JSON.stringify(that.data.ids),//商品ids
                'address_id': that.data.address_id,
                'note': that.data.note,
                'num': that.data.num
            }
        }
        wx.request({
            url: url, //仅为示例，并非真实的接口地址
            method: 'POST',
            data: data,
            header: app.getRequestHeader(),
            success(res) {
                console.log(res.data)

                if (res.data.code == -1) {
                    app.alert({
                        'content': res.data.msg
                    })
                    return
                }

                wx.redirectTo({
                    url: "/pages/my/order_list"
                });
            }
        })
        // wx.showLoading();
    },
    // createOrder: function () {
    //     var that = this;
    //     wx.request({
    //         url:app.buildUrl('/v1/order/create'),
    //         method:'POST',
    //         data:{
    //             'ids':JSON.stringify(that.data.ids),
    //             'address_id':that.data.address_id,
    //             'note':that.data.note,
    //         },
    //         header:app.getRequestHeader(),
    //         success(res) {
    //             if(res.data.code == -1){
    //                 app.alter({'content':res.data.msg})
    //                 return
    //             }
    //            wx.navigateTo({
    //                url: "/pages/my/order_list"
    //            });
    //         }
    //     })
    //     // wx.showLoading();
    // },
    addressSet: function () {
        wx.navigateTo({
            url: "/pages/my/addressSet"
        });
    },
    selectAddress: function () {
        wx.navigateTo({
            url: "/pages/my/addressList"
        });
    },
    getOrderIndex:function(){
        var that = this;
        if (that.data.type == 0) {
            var data = {
                'ids': JSON.stringify(that.data.ids),
                'type': that.data.type
            }
        } else {
            var data = {
                'ids': JSON.stringify(that.data.ids),
                'num': that.data.num,
                'type': that.data.type
            }
        }
        wx.request({
            url:app.buildUrl('/v1/order_shop/index'),
            method:'POST',
            data:data,
            header:app.getRequestHeader(),
            success(res) {
                if(res.data.code == -1){
                    app.alter({'content':res.data.msg})
                    return
                }
                that.setData({
                    goods_list:res.data.data.goods_list,
                    default_address:res.data.data.default_address,
                    address_id:res.data.data.default_address.id,
                    yun_price: res.data.data.yun_price,
                    pay_price:res.data.data.pay_price,
                    total_price: res.data.data.total_price,
                })
            }
        })
    },
    // getOrderInfo:function(){
    //     var that = this;
    //     wx.request({
    //         url:app.buildUrl('/v1/order/info'),
    //         method:'POST',
    //         data:{
    //             'id':that.data.id,
    //             'num':that.data.num,
    //         },
    //         header:app.getRequestHeader(),
    //         success(res) {
    //             if(res.data.code == -1){
    //                 // app.alter({'content':res.data.msg})
    //                 return
    //             }
    //             that.setData({
    //                 goods_list:res.data.data.goods_list,
    //                 default_address:res.data.data.default_address,
    //                 address_id:res.data.data.default_address.id,
    //                 yun_price: res.data.data.yun_price,
    //                 pay_price:res.data.data.pay_price,
    //                 total_price: res.data.data.total_price,
    //             })
    //         }
    //     })
    // },
});
