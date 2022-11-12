var authHeaders = {
    "X-Application-Id": "9e92dc47",
    "X-Api-Key": "ea73781a50a84f6135b7a46ec5b3d03a",
    "Accept-Language": "en-US"
};

var options = {
    // The url for the Autocomplete service
    serviceUrl: "https://api.traveltimeapp.com/v4/geocoding/search",
    ajaxSettings: {
        headers: authHeaders,
        dataType: "json"
    },
    lookupLimit: 5,
    minChars: 2,
    deferRequestBy: 300,
    transformResult: transformGeocodingResult,
}

// Transform the Geocoding result to what autocomplete expects. 
function transformGeocodingResult(response) {
    return {
        suggestions: response.features.map(feature => { return { value: feature.properties.label, data: feature.geometry.coordinates }; })
    }
}

jQuery($ => {
    let inputTemplate = $('#address-input-template').html();

    $('#extra_address').on('click', () => {
        let $content = $(inputTemplate).appendTo('#input_form');
        $content.find('.input_address').autocomplete(options)
    })

    $('.input_address').autocomplete(options)
})