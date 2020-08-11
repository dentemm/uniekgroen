window.onload = function () {

    let section2 = $('#section2').offset().top;
    let section3 = $('#section3').offset().top;
    let section4 = $('#section4').offset().top;

    let section2Text = $('#section2-extra_text');
    let section3Text = $('#section3-extra_text');
    let section4Text = $('#section4-extra_text');

    let current = 0;

    const onScroll = () => {

        current = $(this).scrollTop();

        const section2diff = current - section2;
        const section3diff = current - section3;
        const section4diff = current - section4;

        if (section2diff > 0) {
            section2Text.css({
                opacity: 1
            })
        } else {
            section2Text.css({
                opacity: 0
            }); 
        }

        if (section3diff > 0) {
            section3Text.css({
                opacity: 1
            })
        } else {
            section3Text.css({
                opacity: 0
            }); 
        }

        if (section4diff > 0) {
            section4Text.css({
                opacity: 1
            })
        } else {
            section4Text.css({
                opacity: 0
            }); 
        }
    };

    $(window).scroll(onScroll);
};