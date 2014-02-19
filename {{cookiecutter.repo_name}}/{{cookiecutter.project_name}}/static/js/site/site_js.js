$('a.frontendadmin_edit').hover(
   function(){$(this).parent().css('outline', '4px solid #E9B007')},
   function(){$(this).parent().css('outline', '')}
);

$('a.frontendadmin').click(function(event) {
            event.preventDefault();
            $this = $(this);
            $.get($this.attr('href'), function(data) {
              $('#modalContent').html(data);
            });
});
