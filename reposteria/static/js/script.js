// Función para activar el mapa
function iniciarMap(){
    var coord = {lat:-33.5988 ,lng: -70.7053}; // Variable que tiene las coordenadas (latitud y longitud)
    var map = new google.maps.Map(document.getElementById('map'),{ 
      zoom: 10,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}