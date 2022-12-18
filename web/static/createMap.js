// Start by creating a clean map
function createMap(centreLat, centreLng) {
    if (centreLat == null || centreLng == null) {
        var centreLat = 51.500743
        var centreLng = -0.124658
    };
    map = new google.maps.Map(document.getElementById("map"), {
        center: { 
            lat: centreLat,
            lng: centreLng
        },
        zoom: 15,
        disableDefaultUI: true
    });
    return map
}

// Display source addresses on map
function addSourceMarkers(map, sourceAddresses) {
    var maxZoom = 16
    var bounds = new google.maps.LatLngBounds();
    if (sourceAddresses.length != 0) {
        for (let i = 0; i < sourceAddresses.length; i++) {
            marker = new google.maps.Marker({
                position: {
                    lat: sourceAddresses[i].latitude,
                    lng: sourceAddresses[i].longitude
                },
                map: map
            });
            bounds.extend(marker.getPosition())
        }

        // Set map zoom to cover all source markers
        if (sourceAddresses.length == 1) {
            map.setZoom(maxZoom)
        } else {
            map.fitBounds(bounds, 96)
        }
    }
    return bounds
}

// Adds shell overlays to show overlapping travel area
function addShellOverlays(map, resultLocations) {
    for(let i = 0; i < resultLocations.length; i++) {
        overlay = new google.maps.Polygon({
            paths: resultLocations[i].shell_edges,
            strokeColor: "#878787",
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: "#878787",
            fillOpacity: 0.35,
        });
        overlay.setMap(map);
    }
}

function initMap() {
    // Obtain data from page
    var responseData = $("#response_data_tag").data("key");
    map = createMap(responseData.map_centre.latitude,
                    responseData.map_centre.longitude);
    mapBounds = addSourceMarkers(map, responseData.source_addresses)
    addShellOverlays(map, responseData.result_locations)
}