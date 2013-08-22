
/**
 * Module dependencies.
 */

var express = require('express')
  , routes = require('./routes')
  , nib = require('nib')
  , querystring = require('querystring')
  , stylus = require('stylus')
  , http = require('http')
  , path = require('path');

var app = express()
  , server = http.createServer(app)
  , io = require('socket.io').listen(server);

function compile(str, path) {
  return stylus(str)
    .set('filename', path)
    .set('compress', true)
    .use(nib());
}

// all environments
app.set('port', process.env.PORT || 3030);
app.set('views', __dirname + '/views');
app.set('view engine', 'jade');
app.use(express.favicon());
app.use(express.logger('dev'));

// Middleware.
app.use(stylus.middleware({
  src: __dirname + '/public'
    , compile: compile
  }
));

var theSecret = 'fm@tt9-7i&p#2l4q2*#5jxcr1d5xo4$$0iy@^nk79gi0zg0*71';

app.use(express.bodyParser());
app.use(express.methodOverride());
app.use(express.cookieParser(theSecret));
app.use(express.session());

app.use(app.router);
app.use(express.static(path.join(__dirname, 'public')));

// development only
if ('development' == app.get('env')) {
  app.use(express.errorHandler());
}

// Rutas.
app.get('/', routes.index);
app.get('/areas', routes.areas);

http.createServer(app).listen(app.get('port'), '0.0.0.0', function(){
  console.log('Express server listening on port ' + app.get('port'));
});
