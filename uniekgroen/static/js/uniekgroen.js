window.onload = function () {

    /* ELEMENTS TO CHANGE */
    let navbar = $('.sticky-nav>div').first();
    let titles = $('.sticky-nav').find('div.description');
    let icons = $('.sticky-nav').find('div.icon');

    let text1 = $('#text-1');

    let current = 0;

    const navbarDist = $('.sticky-nav').offset().top;
    let text1Dist = $('#section2-extra').offset().top;

    let canMove = true;
    // const isChrome = !!window.chrome;

    const updateNavbar = (shouldRemove) => {
        
        if (shouldRemove === true) {
            navbar.removeClass('py-5');
            titles.attr('hidden', true);
            icons.addClass('icon-sm');
        } else if (shouldRemove === false) {
            navbar.addClass('py-5');
            titles.attr('hidden', false);
            icons.removeClass('icon-sm');
            canMove = true;
        }
        text1Dist = $('#section2-extra').offset().top;
    }

    const onScroll = () => {

        current = $(this).scrollTop();
        const navbarDiff = current - navbarDist;
        

        /* NAVBAR */
        if (navbar.hasClass('py-5') && navbarDiff > 0) {
            
            updateNavbar(true);

            if (canMove) {
                $(this).scrollTop(navbarDist);
                canMove = false;
            }

        } else if (!navbar.hasClass('py-5') && navbarDiff < 0) {
            updateNavbar(false);
        }

        current = $(this).scrollTop();  

        const text1Diff = current - text1Dist;
        
        /* TEXT 1 */
        if (text1Diff > 0) {
            text1.css('top', `${text1Diff}px`);
        } 

        previous = $(this).scrollTop();
    };

    // const throttle = (func, limit) => {
    //     let lastFunc;
    //     let lastRan;

    //     return function() {
    //         const context = this;
    //         const args = arguments;

    //         if (!lastRan) {
    //             func.apply(context, args);
    //             lastRan = Date.now();

    //         } else {
    //             clearTimeout(lastFunc);
    //             lastFunc = setTimeout(function() {
    //                 if ((Date.now() - lastRan) >= limit) {
    //                     func.apply(context, args)
    //                     lastRan = Date.now()
    //                 }
    //             }, limit - (Date.now() - lastRan));
    //         }
    //     }
    // };

    $(window).scroll(onScroll);
    // $(window).scroll(throttle(onScroll, 50));
};

