$(document).ready(function () {
    $(".property-item").click(function (ev) {
        let datasets = ev.currentTarget.dataset
        let propertyId = datasets.propertyId
        window.location.href = `/property/${propertyId}`
    });
})

function onClickBooking(dataset) {
    propertyId = !dataset.propertyId == true ? 0 : parseInt(dataset.propertyId)
    destinationId = !dataset.destinationId == true ? 0 : parseInt(dataset.destinationId)
    window.location.href = `/booking-step?destination-id=${destinationId}&property-id=${propertyId}`
}