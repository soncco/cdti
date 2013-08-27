(function($) {

  var $lista = $('.lista');

  parseProducto = function(item) {
    $tr = $('<tr></tr>');
    $td = $('<td></td>');
    $editar = $('<a href="#" class="btn btn-info">Editar</a>');

    $td.clone().text(item.unidad_medida).appendTo($tr);
    $td.clone().text(item.descripcion).appendTo($tr);
    $td.clone().html($editar.clone().attr('href', 'productos/editar/' + item.id)).appendTo($tr);

    $tr.appendTo($lista);

  }

  parseProductos = function(data) {
    for(i = 0; i < data.length; i++) {
      parseProducto(data[i]);
    }
  }

  $.ajax({
    url: 'http://192.168.1.35:8000/productos/json',
    dataType: 'jsonp',
    success: function(data) {
      parseProductos(data);
    }
  });
})(jQuery);