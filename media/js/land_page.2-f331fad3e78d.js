function update_height() {
  var top_banner = $("#banner");
  if (top_banner.length) {
    // if banner exists
    top_banner.css("height", "");
    var old_height = top_banner.outerHeight();
    var new_height = window.innerHeight - top_banner.offset().top;
    var height_diff = new_height - old_height;
    if (height_diff > 0 && new_height >= 200 && new_height <= 540) top_banner.css("height", new_height - 10);
  }
}

window.addEventListener("load", function () {
  if ($("#banner").length) {
    // if banner exists
    update_height();
    var orientation = window.innerHeight > window.innerWidth;
    $(window).on("resize", function () {
      var new_orientation = window.innerHeight > window.innerWidth;
      if (new_orientation !== orientation) update_height();
      orientation = new_orientation;
    });
  }
});

document.addEventListener("DOMContentLoaded", function () {
  var fixed_menu = $(".fixed.menu");
  if (fixed_menu.length) {
    // if fixed_menu exists
    $("header").visibility({
      once: false,
      onBottomPassed: function () {
        fixed_menu.transition("fade in");
      },
      onBottomPassedReverse: function () {
        fixed_menu.transition("fade out");
      },
    });
  }

  setTimeout(function () {
    $("#sl-wrapper").transition("swing up", "1000ms");
  }, 100);

  /* no more animation */
  // $('section > div').visibility({
  //     once: true,
  //     onOnScreen: function () {
  //         $(this).transition('scale in', '1300ms');
  //     }
  // });

  // if ($('#banner-left').css('display') !== 'none') {
  //     $('#banner-left').transition({
  //         animation: 'fly left in',
  //         duration: 1700
  //     });
  // }
});
