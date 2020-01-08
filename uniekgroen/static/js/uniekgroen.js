var distance = $('.temm').offset().top;

$(window).scroll(function() {
    if ( $(this).scrollTop() >= distance ) {
        console.log('is in top');
    } else {
        console.log('is not in top');
    }
});