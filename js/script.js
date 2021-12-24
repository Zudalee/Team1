$(function(){
  $('.slides').slick({
    autoplay: true,
    autoplaySpeed: 3000,
  });
});
$(function(){
  $('.slide02').slick({
      centerMode: true,
      centerPadding: '60px',
      slidesToShow: 3,
      responsive: [
      {
          breakpoint: 768,
          settings: {
          arrows: false,
          centerMode: true,
          centerPadding: '40px',
          slidesToShow: 3
          }
      },
      {
          breakpoint: 480,
          settings: {
          arrows: false,
          centerMode: true,
          centerPadding: '40px',
          slidesToShow: 1
          }
      }
      ]
  });
});