$(document).ready(function () {
    $(".property-item").click(function (ev) {
        let datasets = ev.currentTarget.dataset
        let propertyId = datasets.propertyId
        window.location.href = `/property/${propertyId}`
    });
})