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


var score = "";

$(document).ready(function() {
  var score1, score2, score3;
  $('input:radio[name=rate1]').change(function() {
    if (this.value == 'terrible') {
      //alert("you have picked design to be terrible");
      score1 = 2;
      console.log(score1);
      $("#design").text(score1);
    } else if (this.value == 'poor') {
      //alert("you have picked design to be poor");
      score1 = 4;
      console.log(score1);
      $("#design").text(score1);
    } else if (this.value == 'average') {
      //alert("you have picked designto be average");
      score1 = 6;
      console.log(score1);
      $("#design").text(score1);
    } else if (this.value == 'very good') {
      //alert("you have picked design to be very good");
      score1 = 8;
      console.log(score1)
      $("#design").text(score1);
    } else if (this.value == 'excellent') {
      //alert("you have picked design to be excellent");
      score1 = 10;
      console.log(score1)
      $("#design").text(score1);
    }
    $("#id_design").val(score1)
  });

  $('input:radio[name=rate2]').change(function() {
    if (this.value == 'terrible') {
      //alert("you have picked usability to be terrible");
      score2 = 2;
      console.log(score2)
      $("#usability").text(score2);
    } else if (this.value == 'poor') {
      //alert("you have picked usability to be poor");
      score2 = 4;
      console.log(score2)
      $("#usability").text(score2);
    } else if (this.value == 'average') {
      //alert("you have picked usability to be average");
      score2 = 6;
      console.log(score2)
      $("#usability").text(score2);
    } else if (this.value == 'very good') {
      //alert("you have picked usability to be very good");
      score2 = 8;
      console.log(score2)
      $("#usability").text(score2);
    } else if (this.value == 'excellent') {
      //alert("you have picked usability to be excellent");
      score2 = 10;
      console.log(score2)
      $("#usability").text(score2);
    }
    $("#id_usability").val(score2)
  });

  $('input:radio[name=rate3]').change(function() {
    if (this.value == 'terrible') {
      //alert("you have picked creativity to be terrible");
      score3 = 2;
      console.log(score3)
      $("#creativity").text(score3);
    } else if (this.value == 'poor') {
      //alert("you have picked creativity to be poor");
      score3 = 4;
      console.log(score3)
      $("#creativity").text(score3);
    } else if (this.value == 'average') {
      //alert("you have picked creativity to be average");
      score3 = 6;
      console.log(score3)
      $("#creativity").text(score3);
    } else if (this.value == 'very good') {
      //alert("you have picked creativity to be very good");
      score3 = 8;
      console.log(score3)
      $("#creativity").text(score3);
    } else if (this.value == 'excellent') {
      //alert("you have picked creativity to be excellent");
      score3 = 10;
      console.log(score3)
      $("#creativity").text(score3);
    }
    $("#id_creativity").val(score3)
  });

  $("#questions").submit(function(event) {
    event.preventDefault();
    var rated = new Rate;
    // rated.total(score1, score2, score3);
    console.log(rated.total(score1, score2, score3));
    // Rate.average();
    console.log(rated.average());
    $("#id_average").val(rated.average());
    $("#ratingform").submit()
  });
  //business logic
function Rate() {
  this.totalScore = 0;
  this.averageScore = 0;
}
Rate.prototype.total = function(sc1, sc2, sc3) {
  this.totalScore = sc1 + sc2 + sc3;
  return this.totalScore;
}
Rate.prototype.average = function() {
  this.averageScore = (this.totalScore / 3);
  return this.averageScore;
}
});
$('input[name=rate1]').attr('checked',false);
$('input[name=rate2]').attr('checked',false);
$('input[name=rate3]').attr('checked',false);