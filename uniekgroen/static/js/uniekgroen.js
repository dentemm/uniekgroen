window.onload = function () {

    let section2 = 0;
    let section3 = 0;
    let section4 = 0;

    let section2Text = 0;
    let section3Text = 0;
    let section4Text = 0;

    let current = 0;

    const setup = () => {
        section2 = $('#wat-bieden-wij-aan').offset().top;
        section3 = $('#hoe-gaan-wij-te-werk').offset().top;
        section4 = $('#realisaties').offset().top;
    
        section2Text = $('#section2-extra_text');
        section3Text = $('#section3-extra_text');
        section4Text = $('#section4-extra_text');
    }

    const onScroll = () => {

        current = $(this).scrollTop();

        const section2diff = current - section2;
        const section3diff = current - section3;
        const section4diff = current - section4;

        if (section4diff > 0) {
            section4Text.css({ opacity: 1 })
            section3Text.css({ opacity: 0 })
            section2Text.css({ opacity: 0 })

        } else if (section3diff > 0) { 
            section3Text.css({ opacity: 1 })
            section2Text.css({ opacity: 0 })
            section4Text.css({ opacity: 0 })

        } else if (section2diff > 0) {
            section2Text.css({ opacity: 1 })
            section3Text.css({ opacity: 0 })
            section4Text.css({ opacity: 0 })
        }
    };

    setup();

    $(window).scroll(onScroll);
    $(window).resize(setup);
 
};