$(document).ready(function () {
    $('.confirm-booking-button').click(function (ev) {
        ev.preventDefault()
        let customerDetail = $('#customer-detail')
        if (!customerDetail[0].checkValidity()) {
            customerDetail[0].reportValidity()
            return
        }
        let checkIn = $('#checkin-value').text()
        let checkOut = $('#checkout-value').text()
        let totalPrice = $('#total-price-val').text()
        let customerName = $('input#name').val()
        let customerCountry = $('input#country').val()
        let customerEmail = $('input#email').val()
        let customerPhone = $('input#phone').val()
        let customerComment = $('textarea#comment').val()
        let paymentMethodCode = $('select#payment_method').val()
        let propertyId = $('input#property-id').val()

        let extraServices = Array.from($('div.extra-service-item'))
        let extraServiceIds = []
        extraServices.forEach((service) => {
            extraServiceIds.push(parseInt(service.dataset.extraServiceId));
        });

        $.ajax({
            type: "POST",
            url: "/booking/confirmed/",
            data: {
                'check-in': checkIn,
                'check-out': checkOut,
                'total-price': totalPrice,
                'customer-name': customerName,
                'customer-country': customerCountry,
                'customer-email': customerEmail,
                'customer-phone': customerPhone,
                'customer-comment': customerComment,
                'payment-method-code': paymentMethodCode,
                'property-id': propertyId,
                'extra-service-ids': extraServiceIds,
            },
            success: function (data) {
                let confirmationBody = $('body')
                confirmationBody.replaceWith(data);

            }
        })
    });
})