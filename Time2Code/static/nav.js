$(function(){
    // nav收缩展开
    $('.nav-item>a').on('click',function(){
        if (!$('.nav2').hasClass('nav-mini')) {
            if ($(this).next().css('display') == "none") {
                //展开未展开
                $('.nav-item').children('ul').slideUp(300);
                $(this).next('ul').slideDown(300);
                $(this).parent('li').addClass('nav-show').siblings('li').removeClass('nav-show');
            }else{
                //收缩已展开
                $(this).next('ul').slideUp(300);
                $('.nav-item.nav-show').removeClass('nav-show');
            }
        }
    });
    //nav-mini切换
    $('#mini').on('click',function(){
        if (!$('.nav2').hasClass('nav-mini')) {
            $('.nav-item.nav-show').removeClass('nav-show');
           // $('.panel-container').removeClass('col-md-10');
           // $('.panel-container').addClass('col-md-11');
            $('.nav-item').children('ul').removeAttr('style');
            $('.nav2').addClass('nav-mini');
        }else{
            $('.nav2').removeClass('nav-mini');
            //$('.panel-container').removeClass('col-md-11');
           // $('.panel-container').addClass('col-md-10');
        }
    });
});