function bindCaptchaBtnClick(){
    $("#captcha-btn").on("click", function (event){
       var $this = $(this);
       var email = $("input[name='email']").val();
       if(!email){
           alert("请先输入邮箱！")
           return;
       }
       //通过js发送网络请求：ajax
        $.ajax({
            url: "/user/captcha",
            method: "POST",
            data: {
                "email":email
            },
            success: function (res){
                var code = res['code'];
                if(code == 200){
                    //取消点击事件
                    $this.off("click");
                    //开始倒计时
                    var countDown = 60;
                    var timer = setInterval(function (){
                        if(countDown > 0){
                            $this.text(countDown+"秒后重新发送");
                        }else{
                            $this.text("获取验证码");
                            //重新执行下这个函数
                            bindCaptchaBtnClick();
                            //清楚倒计时
                            clearInterval(timer);
                        }
                        countDown -= 1;
                    }, 1000);
                    alert("验证码发送成功");
                }else{
                    alert(res['message']);
                }
            }
        })
    });
}

//等网页文档所有权元素都加载完成后再执行
$(function (){
    bindCaptchaBtnClick();
});