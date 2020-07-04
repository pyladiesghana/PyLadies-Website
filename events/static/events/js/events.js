$('a[data-toggle="list"]').on('shown.bs.tab', function (e) {
  $(e.target).removeClass( "light-blue" );
  $(e.relatedTarget).addClass( "light-blue" );
})