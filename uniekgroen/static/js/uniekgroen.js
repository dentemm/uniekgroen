window.onload = function () {

    let distance = $('.sticky-nav').offset().top;
    let canMove = true;
    // const isChrome = !!window.chrome;

    const changeNavBar = () => {
        let el = $('.sticky-nav>div').first();
        let titles = $('.sticky-nav').find('div.description');
        let icons = $('.sticky-nav').find('div.icon');

        if ( $(this).scrollTop() >= distance) {
            el.removeClass('py-5');
            titles.attr('hidden', true);
            icons.addClass('icon-sm');

            if (canMove) {
                $(this).scrollTop(distance);
                canMove = false;
            }

        } else if (!el.hasClass('py-5')) {
            el.addClass('py-5');
            titles.attr('hidden', false);
            icons.removeClass('icon-sm');

            canMove = true;
        } 
    };

    $(window).scroll(changeNavBar);
};

