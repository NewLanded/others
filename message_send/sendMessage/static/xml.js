'use strict'

function sendXml(obj){
    var nowid = obj.id;
    var xml = $('#'+nowid).parent().next().children().get(0).value;
    Request('/sendOneXml/',{'xml':xml},xmlTip);
}

function sendNatp(obj){
    var nowid = obj.id;
    var natp = $('#'+nowid).parent().next().children().get(0).value;
    Request('/sendOneNatp/',{'natp':natp},natpTip);
}

function xmlTip(data){
    alert(data);
}

function natpTip(data){
    alert(data);
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
