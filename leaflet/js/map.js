// On initialise la latitude et la longitude de Paris (centre de la carte)
var lat = 48.852969,
  lon = 2.349903; // Paris
var map = null;
var lat_lon = {};
  
d3.json("data/countries.json").then(function(countries) {
  for (var i in countries)
  {
    var country = countries[i];
    lat_lon[country.COUNTRY] = {
      'lat': country.LATITUDE,
      'lon': country.LONGITUDE
    }
  }  

  d3.json("data/attacks-details.json").then(function(data) {
    var mbAttr =
        'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      mbUrl =
        "https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw";

    var grayscale = L.tileLayer(mbUrl, {
      id: "mapbox.light",
      attribution: mbAttr
    });

    var streets = L.tileLayer(mbUrl, {
      id: "mapbox.streets",
      attribution: mbAttr
    });

    var baseLayers = { Grayscale: grayscale, Streets: streets };

    map = L.map("map", {
      center: [lat, lon],
      zoom: 2,
      layers: [grayscale]
    });

    var points = L.markerClusterGroup();
    L.control.layers(baseLayers).addTo(map);
    points.addTo(map);

    for (var i in data) {
      var country = data[i].country_short;
      var latitude = lat_lon[country].lat;
      var longitude = lat_lon[country].lon;

      var marker = L.marker([latitude, longitude]);
      marker.addTo(points);
      marker.bindPopup(makePopup(data[i]));
    }
  });
});

function makePopup(fields) {
  var popup = "";
  popup = "<h1>IP: " + fields.ip + "</h1>";
  popup += "<b>Attacks: " + fields.attack + "</b>";
  popup += "<br/>";
  return popup;
}
