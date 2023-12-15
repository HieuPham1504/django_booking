$(document).ready(function () {
    $('.booking-detail-row').click(function (ev) {
        let currentRow = ev.currentTarget.dataset
        let bookingId = parseInt(currentRow.bookingId)
        window.location.href = `/booking/${bookingId}`
    })
})