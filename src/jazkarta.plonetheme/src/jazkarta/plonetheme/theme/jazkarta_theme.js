jQuery(function($) {
    function adjust_full_width() {
        var window_width = $('body').width();
        var $rows = $('.row.tile-fullwidth, #related-slider-wrapper');
        var width = $rows.outerWidth(true);
        var new_margin = -(window_width - width)/2;
        $rows.css('margin-left', new_margin).css('margin-right', new_margin);
    }
    adjust_full_width();
    $(window).resize(adjust_full_width);
    var $container = $('#related-slider');
    var $related_slider = $container.find('.slider');
    if ($related_slider.length) {
        $container.find('.next, .prev').unbind('click');
        var scr_api = $related_slider.data('scrollable');
        $container.find('.next').click(function () {
            scr_api.move(2);
        });
        $container.find('.prev').click(function () {
            scr_api.move(-2);
        });
    }
});
