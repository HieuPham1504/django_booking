$(document).ready(function () {
    $('.js_date_picker').datepicker({
        dateFormat: 'dd/mm/yy',
        useCurrent: false,
        keepOpen: false,
        icons: {
            time: 'fa fa-clock-o',
            date: 'fa fa-calendar',
            up: 'fa fa-chevron-up',
            down: 'fa fa-chevron-down',
            previous: 'fa fa-chevron-left',
            next: 'fa fa-chevron-right',
            today: 'fa fa-calendar-check-o',
            clear: 'fa fa-trash',
            close: 'fa fa-check primary',
        },
        buttons: {
            showToday: true,
            showClear: false,
            showClose: true,
        },
    });

    let slideIndex = 0;
    showSlides();

    function showSlides() {
        let i;
        let slides = document.getElementsByClassName('mySlides');
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = 'none';
        }
        slideIndex++;
        if (slideIndex > slides.length) {
            slideIndex = 1
        }
        if (slides) {
            slides[slideIndex - 1].style.display = 'block';
            setTimeout(showSlides, 2000);
        }
    };

    $('input.submit').click(function (ev) {
        ev.preventDefault()
        let self = this
        let propertyId = parseInt($('#property-id').val())
        let checkIn = $('#checkin').val()
        let checkOut = $('#checkout').val()
        let noGuest = $('#no_guest').val() == '' ? 0 : parseInt($('#no_guest').val())
        $.ajax({
            type: "POST",
            url: "/booking/available_reservations/",
            data: {
                property_id: propertyId,
                check_in: checkIn,
                check_out: checkOut,
                no_guest: noGuest,
            },
            success: function (data) {
                let availableDiv = $('div.available-reservation')
                let bookingStepDiv = $('div.booking-step')
                let extraServices = $('#extra-services')
                availableDiv.replaceWith(data);
                bookingStepDiv.css('display', 'flex')
                extraServices.css('display', 'none')
            }
        })
    });

    $('.dropdown-icon').click(function (ev) {
        let benefitsContainer = $("div.benefits-container")
        benefitsContainer.toggleClass('active-service')
    })


})

function onClickBooking() {
    let extraServices = $('#extra-services')
    let availableReservation = $('.available-reservation')
    let bookingStepDiv = $('div.booking-step')

    extraServices.css('display', 'block')
    availableReservation.css('display', 'none')
    bookingStepDiv.css('height', '400px')
    bookingStepDiv.css('padding-bottom', '80px')

}

function onClickAddExtraServices() {
    let currentTarget = $(event.currentTarget)
    currentTarget.toggleClass('selected-button')
    currentTarget.closest('.extra-service-item').toggleClass('selected-service')
}

function onClickBookingPayment() {
    let propertyId = $('input#property-id').val()
    let checkIn = $('input#checkin').val()
    let checkOut = $('input#checkout').val()
    let totalAmount = $('span#total-amount').text()
    let selectedServices = Array.from($('div.selected-service'))
    let extraServiceIds = []
    selectedServices.forEach((service) => {
        extraServiceIds.push(service.dataset.serviceId);
    });

    window.location.href = `/booking/confirmation?property-id=${propertyId}&check-in=${checkIn}&check-out=${checkOut}&total-amount=${totalAmount}&extra-service-ids=${extraServiceIds}`
}