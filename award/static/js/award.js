$(document).ready(function () {
    var $nav = $('.navbar');
    var $bars = $('#bars');
    var $closeBtn = $('.closeBtn');
    var $main = $('#main');
    
    $bars.click(function () {
      $nav.css('width', "250px");
      $main.css({'marginLeft':'250px'});
      $('body').css('backgroundColor',"rgba(0,0,0,0.4)")
    });
    $closeBtn.click(function () {
      $nav.css('width', '0');
      $main.css('marginLeft', '0');
      $('body').css('backgroundColor',"rgba(0,0,0,0)")
    })
    
  });