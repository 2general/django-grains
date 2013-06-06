(function($) {
    $(document).ready(function() {
        $('.grp-changelist-results tbody tr td:nth-child(3)').on('click', function() {
            var link = $(this).prev().find('a');
            window.location = link.attr('href');
            return false;
        });
    });
})(django.jQuery);
