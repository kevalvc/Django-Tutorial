$(function () {

    // animate on scroll
    new WOW().init();
    $('.counter').counterUp({
      delay:10,
      time: 3000
    });
    $(".image_slider").slick({
    	dots: true,
       arrows: true,
       autoplay: true
    });

});

$(function(){
   $("#customer-testimonials").owlCarousel({
      items: 1,
      autoplay: true,
      loop: true,
      smartSpeed: 700,
      autoplayHoverPause: true
   });
})


/*   stats    */
$(function(){

})

/* slider */

$(document).ready(function(){


});


$(document).ready(function(){

});
$(document).ready(function(){

});

$(function(){
})


$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})

/*==================================
            TEAM
==================================*/

$(function(){
   $("#team-members").owlCarousel({
      items: 4,
      autoplay: true,
      loop: false,
      smartSpeed: 700,
      autoplayHoverPause: true
   });
})
