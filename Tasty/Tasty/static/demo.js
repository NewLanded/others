'use strict'

$(document).mouseover(function(e){
    var nowId=$(e.target).attr('id');
    var a=$('#'+nowId);
    var c=a.prev();
    var d=a.parent();

    a.mouseenter(function(){
        c.css('display','inline');
    });

    d.mouseleave(function(){
        c.css('display','none');
    })
});