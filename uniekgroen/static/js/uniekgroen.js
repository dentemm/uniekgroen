window.onload = function () {

    let distance = $('.sticky-nav').offset().top;

    $(window).scroll(function() {

        let el = $('.sticky-nav>div').first();
        let titles = $('.sticky-nav').find('div.description');
        let icons = $('.sticky-nav').find('div.icon');

        if ( $(this).scrollTop() >= distance ) {
            el.removeClass('py-5');
            titles.attr('hidden', true);
            icons.addClass('icon-sm');
        } else if (!el.hasClass('py-5')) {
            el.addClass('py-5');
            titles.attr('hidden', false);
            icons.removeClass('icon-sm');
        }
    });
};

