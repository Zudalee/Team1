$(function () {
  $('.slides').slick({
    autoplay: true,
    autoplaySpeed: 3000,
  });
});
$(function () {
  $('.slide02').slick({
    centerMode: true,
    centerPadding: '50px',
    slidesToShow: 3,
    autoplay: true,
    autoplaySpeed: 3000,
    responsive: [
      {
        breakpoint: 768,
        settings: {
          arrows: false,
          centerMode: true,
          centerPadding: '50px',
          slidesToShow: 3
        }
      },
      {
        breakpoint: 480,
        settings: {
          arrows: false,
          centerMode: true,
          centerPadding: '50px',
          slidesToShow: 1
        }
      }
    ]

  });
});