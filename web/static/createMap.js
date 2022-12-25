// Start by creating a clean map
function createMap(centreLat, centreLng) {
    if (centreLat == null || centreLng == null) {
        var centreLat = 51.4780
        var centreLng = 0
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
    allShellBounds = [];
    for(let i = 0; i < resultLocations.length; i++) {
        var shellBounds = new google.maps.LatLngBounds()
        overlay = new google.maps.Polygon({
            paths: resultLocations[i].shell_edges,
            strokeColor: "#878787",
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: "#878787",
            fillOpacity: 0.35,
        });
        overlay.setMap(map);
        overlay.getPath().forEach(element => {
            shellBounds.extend(element);
        })
        allShellBounds.push(shellBounds)
    }
    return allShellBounds
}

// Remove all unwanted places from results - e.g. car parks and similar things
function filterPlaceResults(results) {
    var desiredTypes = ["amusement_park", "aquarium", "art_gallery", "bar", "movie_theater", "bowling_alley", "museum", "cafe", "night_club", "park", "casino", "restaurant", "shopping_mall", "spa", "tourist_attraction", "zoo"]
    var filteredResults = []
    for (let i = 0; i < results.length; i++) {
        results[i].types = results[i].types.filter(value => desiredTypes.includes(value));
        if (results[i].types.length > 0) {
            filteredResults.push(results[i]);
        }
    }
    return filteredResults
}

function setRating(element, value) {
    roundedValue = Math.round(value)
    fullStars = Math.floor(value)
    halfStars = Math.abs(Math.round(value) - value) > 0.25 ? 1 : 0
    emptyStars = 5 - halfStars - fullStars
    console.log(value)
    appendHtml = "<i class=\"fa fa-star\" aria-hidden=\"true\"></i>".repeat(fullStars) +
                 "<i class=\"fa fa-star-half-o\" aria-hidden=\"true\"></i>".repeat(halfStars) +
                 "<i class=\"fa fa-star-o\" aria-hidden=\"true\"></i>".repeat(emptyStars)
    element.html(appendHtml)
}

function setPrice(element, value) {
    if (value != undefined) {
        element.html(
            "<i class=\"fa fa-gbp\" aria-hidden=\"true\"></i>".repeat(value)
        );
    }
}

function setLocationType(element, value) {
    // TODO: Pick most relevant type instead of first
    element.html(value[0])
}

function setAddress(element, value) {
    element.html(value)
}

function writeResultsToCard(resultTemplate, results) {
    results.forEach(result => {
        jQuery($ => {
            var $elem = $(resultTemplate);
            console.log(result.name)
            $elem.find(".place_name").html(result.name);
            setRating($elem.find(".rating"), result.rating);
            setPrice($elem.find(".price"), result.price_level);
            setLocationType($elem.find(".type"), result.types);
            setAddress($elem.find(".address"), result.vicinity);
            $($elem).appendTo('#card_content')
        })
    })
}

function callback(results, status, pagination) {
    if (status == google.maps.places.PlacesServiceStatus.OK) {
        let resultTemplate = $('#place-results-template').html();
        filteredResults = filterPlaceResults(results)
        writeResultsToCard(resultTemplate, filteredResults)
        if (filteredResults.length < 5 && pagination && pagination.hasNextPage) {
            pagination.nextPage();
        }
    }
}

// Search for places of interest at centre of each shell. 
// If there isn't much in the shell, it might go outside it.
function findPlacesOfInterest(map, shellBounds) {
    for (let i = 0; i < shellBounds.length; i++) {
        var request = {
            bounds: shellBounds[i],
            rankBy: google.maps.places.RankBy.PROMINENCE,
        };
        service = new google.maps.places.PlacesService(map);
        service.nearbySearch(request, callback);
    }
}

function initMap() {
    // Obtain data from page
    var responseData = $("#response_data_tag").data("key");
    map = createMap(responseData.map_centre.latitude,
                    responseData.map_centre.longitude);
    mapBounds = addSourceMarkers(map, responseData.source_addresses)
    shellBounds = addShellOverlays(map, responseData.result_locations)
    findPlacesOfInterest(map, shellBounds)
}