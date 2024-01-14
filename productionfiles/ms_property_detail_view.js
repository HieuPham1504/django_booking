$(document).ready(function () {
    $('.buttonPropertyBooking').click(function (ev) {
        let propertyId = $('input#property-id').val();
        let destinationId = $('input#destination-id').val();
        location.replace(`${location.origin}/booking-step/?destination-id=${destinationId}&property-id=${propertyId}`)
    })
})