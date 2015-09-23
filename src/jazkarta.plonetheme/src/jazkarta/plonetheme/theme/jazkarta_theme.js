jQuery(function($) {
    function adjust_full_width() {
        var window_width = $('body').width();
        var $rows = $('.row.tile-fullwidth');
        var width = $rows.outerWidth(true);
        var new_margin = -(window_width - width)/2;
        $rows.css('margin-left', new_margin).css('margin-right', new_margin);
    }
    adjust_full_width();
    $(window).resize(adjust_full_width);
});
