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

  var timer;
var timerFinish;
var timerSeconds;

function drawTimer(c, a) {
  $("#pie_" + c).html('<div class="percent"></div><div id="slice"' + (a > 5 ? ' class="gt50"' : "") + '><div class="pie"></div>' + (a > 5 ? '<div class="pie fill"></div>' : "") + "</div>");
  var b = 360 / 10 * a;
  $("#pie_" + c + " #slice .pie").css({
    "-moz-transform": "rotate(" + b + "deg)",
    "-webkit-transform": "rotate(" + b + "deg)",
    "-o-transform": "rotate(" + b + "deg)",
    transform: "rotate(" + b + "deg)"
  });
  a = Math.floor(a * 100) / 100;
  arr = a.toString().split(".");
  intPart = arr[0];
  dec = arr[1];
  if (!dec > 0) {
    dec = 0
  }
  $("#pie_" + c + " .percent").html('<span class="int">' + intPart + '</span><span class="dec">.' + dec + "</span>")
}
function stoppie(d, b) {
  var c = (timerFinish - (new Date().getTime())) / 1000;
  var a = 10 - ((c / timerSeconds) * 10);
  a = Math.floor(a * 100) / 100;
  if (a <= b) {
    drawTimer(d, a)
  } else {
    b = $("#pie_" + d).data("pie");
    arr = b.toString().split(".");
    $("#pie_" + d + " .percent .int").html(arr[0]);
    $("#pie_" + d + " .percent .dec").html("." + arr[1])
  }
}
$(document).ready(function() {
  timerSeconds = 3;
  timerFinish = new Date().getTime() + (timerSeconds * 1000);
  $(".piesite").each(function(a) {
    pie = $("#pie_" + a).data("pie");
    timer = setInterval("stoppie(" + a + ", " + pie + ")", 0)
  })
});