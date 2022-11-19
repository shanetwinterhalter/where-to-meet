var options = {
    // The url for the Autocomplete service
    serviceUrl: "/autocomplete",
    ajaxSettings: {
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
    let tooManyAddresses = $('#max-addresses-template').html();

    $('#extra_address').on('click', () => {
        let addressCount = $('.input-group').length
        if (addressCount < 13) {
            let $content = $(inputTemplate).appendTo('#input_form');
            $content.find('.input_address').autocomplete(options)
        } else if ($('#address-warning').length == 0) {
            $(tooManyAddresses).appendTo('#input_form');
        }
    })

    $('.input_address').autocomplete(options)
})