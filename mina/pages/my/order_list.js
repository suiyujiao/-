var app = getApp();
Page({
    data: {
        statusType: ["待付款", "待发货", "待收货", "待评价", "已完成", "已关闭"],
        status: ["-8", "-7", "-6", "-5", "1", "0"],
        currentType: 0,
        tabClass: ["", "", "", "", "", ""]
    },
    statusTap: function (e) {
        var curType = e.currentTarget.dataset.index;
        this.data.currentType = curType;
        this.setData({
            currentType: curType
        });
        this.onShow();
    },
    orderDetail: function (e) {
        wx.redirectTo({
            url: "/pages/my/order_info?order_sn="+e.currentTarget.dataset.id
        })
    },
    onLoad: function (options) {
        // 生命周期函数--监听页面加载
    },
    onReady: function () {
        // 生命周期函数--监听页面初次渲染完
    },
    onShow: function () {
        var that = this;
        that.setData({
            // order_list: [
            //     {
            // 		status: -8,
            //         status_desc: "待支付",
            //         date: "2018-07-01 22:30:23",
            //         order_number: "20180701223023001",
            //         note: "记得周六发货",
            //         total_price: "85.00",
            //         goods_list: [
            //             {
            //                 pic_url: "/images/food.jpg"
            //             },
            //             {
            //                 pic_url: "/images/food.jpg"
            //             }
            //         ]
            //     }
            // ]
        });
        this.getOrderList()
    },
    onHide: function () {
        // 生命周期函数--监听页面隐藏

    },
    onUnload: function () {
        // 生命周期函数--监听页面卸载

    },
    onPullDownRefresh: function () {
        // 页面相关事件处理函数--监听用户下拉动作

    },
    onReachBottom: function () {
        // 页面上拉触底事件的处理函数

    },
    getOrderList: function () {
        var that = this;
        wx.request({
            url: app.buildUrl('/v1/order/list'),
            method: 'GET',
            data: {
                'status': that.data.status[this.data.currentType]
            },

            header: app.getRequestHeader(),
            success(res) {
                if (res.data.code == -1) {
                    // app.alter({'content':res.data.msg})
                    // return
                }
                that.setData({
                    order_list: res.data.data.order_list,
                })
            }
        })
    },
    pay: function (e) {
        var order_sn = e.currentTarget.dataset.id
        var that = this;
        wx.request({
            url: app.buildUrl('/v1/order/pay'),
            method: 'GET',
            header: app.getRequestHeader(),
            data: {
                'order_sn': order_sn
            },
            success(res) {
                var data = res.data
                if (res.data.code == -1) {
                    app.alter({'content': res.data.msg})
                    return
                }
                wx.requestPayment(
                    {
                        'timeStamp': res.data.data.pay_info.timeStamp,
                        'nonceStr': res.data.data.pay_info.nonceStr,
                        'package': res.data.data.pay_info.package,
                        'signType': 'MD5',
                        'paySign': res.data.data.pay_info.paySign,
                        'success': function (res) {
                        },
                        'fail': function (res) {
                        },
                        'complete': function (res) {
                        }
                    })
            }
        })
    },
    goComment: function (e) {
        wx.navigateTo({
            url: '/pages/my/comment?id=' + e.currentTarget.dataset.id
        })
    },
    cancel: function (e) {
        var that = this;
        var order_sn = e.currentTarget.dataset.id;
        wx.request({
            url: app.buildUrl('/v1/order/cancel'),
            method: 'POST',
            data: {
                'order_sn': order_sn,
            },
            header: app.getRequestHeader(),
            success(res) {
                if (res.data.code == -1) {
                    app.alert({'content': res.data.msg});
                    return
                }
                app.alert({'content': res.data.msg});
                return
            }
        })
    },
    // 确认收货
    notarize: function (e) {
        var that = this;
        var order_sn = e.currentTarget.dataset.id;
        wx.request({
            url: app.buildUrl('/v1/order/notarize'),
            method: 'POST',
            data: {
                'order_sn': order_sn,
            },
            header: app.getRequestHeader(),
            success(res) {
                if (res.data.code == -1) {
                    app.alert({'content': res.data.msg});
                    return
                }
                app.alert({'content': res.data.msg});
                return
            }
        });
        // wx.redirectTo({
        //     url: "/pages/my/comment?order_sn=" +e.order_sn
        // })
    },
})

