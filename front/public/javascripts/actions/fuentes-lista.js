(function($) {

  var $lista = $('.lista');

  parseFuente = function(item) {
    $tr = $('<tr></tr>');
    $td = $('<td></td>');
    $editar = $('<a href="#" class="btn btn-info">Editar</a>');

    $td.clone().text(item.nombre).appendTo($tr);
    $td.clone().html($editar.clone().attr('href', 'fuentes/editar/' + item.id)).appendTo($tr);

    $tr.appendTo($lista);

  }

  parseFuentes = function(data) {
    for(i = 0; i < data.length; i++) {
      parseFuente(data[i]);
    }
  }

  $.ajax({
    url: 'http://192.168.1.35:8000/fuentes/json',
    dataType: 'jsonp',
    success: function(data) {
      parseFuentes(data);
    }
  });
})(jQuery);