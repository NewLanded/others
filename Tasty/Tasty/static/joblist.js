'use strict';

$('.list-group-item').click(function(){
        var nowId = $(this).attr('id');
        Request('/job/getJobInfo/',{'id':nowId},getJonInfo);
});
function getJonInfo(jobInfo){
    var jobInfo = JSON.parse(jobInfo);
    var ulid = '#ul'+jobInfo['id'];
    var jobInfoNameList = ['jobBasicInformation','jobAttract','jobDescription'];
    $('.menu').css('display','none'); //将所有的ul隐藏
    $(ulid).css('display','block').children().remove(); //将ul框显示出来，并将ul下的li都删除，避免重复添加
    $.each(jobInfoNameList,function(key,item){
        var jobInfoValueHtml = '<li class="jobLi">'+jobInfo[item]+'</li>';
        $(ulid).append(jobInfoValueHtml);
    });
    var emailElement = "<form id='email'><input type='text' name='email' id='input"+jobInfo['id']+"'><button type='button' onclick='sendEmail(this)' id='aaa'>发送邮件</button></form>";
    $(ulid).append(emailElement);
}

function sendEmail(obj){
    var nowid = obj.id;
    var id = $('#'+nowid).parent().parent().prev().children().get(0).id;  //获取数据库中数据的id
    var emailAddress = $('#'+nowid).prev().val();
    Request('/job/sendEmail/',{'id':id,'emailAddress':emailAddress},emailTip);
}

function emailTip(){
    alert('邮件已发送');
}

function Request(url,regionId,bindFunc) {
    $.ajax({
        type: 'POST',
        url: url,
        data: regionId,
        cache: false,
        async: true,
        success: bindFunc
    });
};





