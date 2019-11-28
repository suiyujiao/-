//获取应用实例
var app = getApp();
Page({
    data: {
        "content":"",
        "score":10,
        // "order_sn":""
    },
    onLoad: function (e) {
        // console.log(e,'eeeeeeeeeeeeeee')
        this.setData({
            order_sn:e.id
            // order_sn:e.order_sn
        })
    },
    scoreChange:function(e){
        this.setData({
            "score":e.detail.value
        });
    },
    inputchange:function(e){
        this.setData({
            content:e.detail.value
        })
    },

    doComment:function(){
        var that = this;
        wx.request({
            url: app.buildUrl("/v1/comment/add"),
            method:'POST',
            header: app.getRequestHeader(),
            data:{
                content:that.data.content,
                score:that.data.score,
                order_sn:that.data.order_sn,
            },
            success: function (res) {
                var res = res.data;
                if (res.code != 1) {
                    app.alert({"content": res.msg});
                    return;
                }
                wx.navigateBack({
                    deita:-1
                })
            }
        });
    },
    Comment:function () {
        var that = this;
        wx.request({
            url: app.buildUrl("/my/comment/list1"),
            header: app.getRequestHeader(),
            success: function (res) {
                var resp = res.data;
                if (resp.code != 1) {
                    app.alert({"content": resp.msg});
                    return;
                }
                that.setData({
                    commentList:that.data.data.commentList,
                });
            }
        });
    }
});