(function($) {

  var $lista = $('.lista');

  parseArea = function(item) {
    $tr = $('<tr></tr>');
    $td = $('<td></td>');
    $editar = $('<a href="#" class="btn btn-info">Editar</a>');

    $td.clone().text(item.nombre).appendTo($tr);
    $td.clone().html($editar.clone().attr('href', 'areas/editar/' + item.id)).appendTo($tr);

    $tr.appendTo($lista);

  }

  parseAreas = function(data) {
    for(i = 0; i < data.length; i++) {
      parseArea(data[i]);
    }
  }

  $.ajax({
    url: 'http://192.168.1.35:8000/areas/json',
    dataType: 'jsonp',
    success: function(data) {
      parseAreas(data);
    }
  });
})(jQuery);