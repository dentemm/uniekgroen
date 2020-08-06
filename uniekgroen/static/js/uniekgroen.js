window.onload = function () {

    /* ELEMENTS TO CHANGE */
    let navbar = $('#nav')

    let text1 = $('#text-1');
    let text2 = $('#text-2');

    let current = 0;

    const bodyHeight = document.body.scrollHeight;

    const onScroll = () => {

        if (document.documentElement.scrollTop >= bodyHeight) {return}

        const navbarDist = navbar.offset().top;
        let text1Dist = $('#section2-extra').offset().top;
        let text2Dist = $('#section3-extra').offset().top;

        current = $(this).scrollTop();
        const navbarDiff = current - navbarDist;

        /* NAVBAR */
        if (navbarDiff >= 0) {
            navbar.removeClass('bg-dark');
            navbar.css('background-color', 'rgba(52, 58, 64, 0.6)');

        } else {
            if (!navbar.hasClass('bg-dark')) {
                navbar.addClass('bg-dark');
                navbar.removeAttr('style');
            }
        }

        const text1Diff = current - text1Dist;
        const text2Diff = current - text2Dist;
        
        /* TEXT 1 */
        if (text1Diff > 0) {
            text1.css('top', `${text1Diff}px`);
        }

        if (text2Diff > 0) {
            text2.css('top', `${text2Diff}px`);
        } 
    };

    // $(window).scroll(onScroll);
};
