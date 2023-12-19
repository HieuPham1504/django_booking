$(document).ready(function () {
    $('.booking-detail-row').click(function (ev) {
        let currentRow = ev.currentTarget.dataset
        let bookingId = parseInt(currentRow.bookingId)
        window.location.href = `/booking/${bookingId}`
    })

    $('#filter-type').change(function () {
        let data = $(this).val();
        let dateInput = $('.date-input')
        let bookingCodeInput = $('.booking-code-input')
        let partnerTypeInput = $('.partner-type-input')
        let partnerTypeIndividualValue = $('.partner-type-individual-value')
        let partnerTypeAgencyValue = $('.partner-type-agency-value')
        // alert(data);
        filterDate = ['check_in', 'check_out']
        if (filterDate.includes(data)) {
            bookingCodeInput.css('display', 'none')
            partnerTypeInput.css('display', 'none')
            partnerTypeIndividualValue.css('display', 'none')
            partnerTypeAgencyValue.css('display', 'none')
            dateInput.fadeIn()
        }
        else if (data == 'booking_code') {
            dateInput.css('display', 'none')
            partnerTypeInput.css('display', 'none')
            bookingCodeInput.fadeIn()
            partnerTypeIndividualValue.css('display', 'none')
            partnerTypeAgencyValue.css('display', 'none')
        }
        else if (data == 'partner_type') {
            dateInput.css('display', 'none')
            bookingCodeInput.css('display', 'none')
            partnerTypeInput.fadeIn()

        }
    });

    $('#partner-type').change(function () {
        debugger
        let data = $(this).val();
        let partnerTypeIndividualValue = $('.partner-type-individual-value')
        let partnerTypeAgencyValue = $('.partner-type-agency-value')
        if ( data == 'individual' ) {
            partnerTypeAgencyValue.css('display', 'none')
            partnerTypeIndividualValue.fadeIn()
        }
        else if ( data == 'agency' ) {
            partnerTypeIndividualValue.css('display', 'none')
            partnerTypeAgencyValue.fadeIn()
        }
        else {
            partnerTypeAgencyValue.css('display', 'none')
            partnerTypeIndividualValue.css('display', 'none')
        }
    })
})