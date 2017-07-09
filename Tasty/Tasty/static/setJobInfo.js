'use strict';

function setJobInfo(obj){
    var nowid = obj.id;
    var jobName = $('#'+nowid).prev().val();
    Request('/job/setJobInfo/',{'jobName':jobName},Tip);
}

function Tip(returnInfo){
    var returnInfo = JSON.parse(returnInfo);
    if (returnInfo["setStatus"]){
        alert('OK');
    }
    else{
        alert('ERROR');
    }
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
}



