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
    // Move two items at a time in scroller
    var $related_slider = $('#related-slider .slider');
    if ($related_slider.length) {
        var scr_api = $related_slider.data('scrollable');
        $('#related-slider .next').click(scr_api.next);
        $('#related-slider .prev').click(scr_api.prev);
    }
});
