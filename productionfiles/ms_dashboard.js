$(document).ready(function () {

    let slidePageNumberLimit = 3

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

    // showSlides();

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
        slides[slideIndex - 1].style.display = 'block';
        setTimeout(showSlides, 2000); // Change image every 2 seconds
    }

    function getCurrentDisplayDestination() {
        let displayDestinations = $('li.slider-item-active')

        let displayDestinationIds = []
        Array.from(displayDestinations).forEach((destination) => {
            displayDestinationIds.push(parseInt(destination.dataset.destinationId));
        });
        return displayDestinationIds
    }

    function hideCurrentDisplayDestination() {
        let displayDestinations = $('li.slider-item-active')
        displayDestinations.removeClass('slider-item-active');
        displayDestinations.addClass('slider-item');
    }

    function getNotDisplayDestination() {
        let notDisplayDestinations = $('li.slider-item')

        let notDisplayDestinationIds = []
        Array.from(notDisplayDestinations).forEach((destination) => {
            notDisplayDestinationIds.push(parseInt(destination.dataset.destinationId));
        });
        return notDisplayDestinationIds.sort()
    }

    function displayDestination(destinationIds) {
        destinationIds.forEach((destination_id) => {
            let sliderItem = $(`*[data-destination-id=${destination_id}]`);
            sliderItem.removeClass('slider-item');
            sliderItem.addClass('slider-item-active');
        })
    }

    // slider
    $("#next").click(function () {
        console.log('click next updateda')
        let displayDestinationsIds = getCurrentDisplayDestination()
        if (displayDestinationsIds.length > 0) {
            let maxDisplayDestinationId = Math.max(...displayDestinationsIds)
            let notDisplayDestinationIds = getNotDisplayDestination()
            if (notDisplayDestinationIds.length > 0) {
                let nextDestination_ids = []
                notDisplayDestinationIds.forEach((destination_id) => {
                    if (destination_id > maxDisplayDestinationId && nextDestination_ids.length < 3) {
                        nextDestination_ids.push(destination_id)
                    }
                })
                if (nextDestination_ids.length > 0) {
                    hideCurrentDisplayDestination()
                    displayDestination(nextDestination_ids)
                }
            }

        }
    });

    $('#previous').click(function () {
        console.log('click previous')
        let displayDestinationsIds = getCurrentDisplayDestination()
        if (displayDestinationsIds.length > 0) {
            let minDisplayDestinationId = Math.min(...displayDestinationsIds)
            let notDisplayDestinationIds = getNotDisplayDestination()
            if (notDisplayDestinationIds.length > 0) {
                let prevDestination_ids = []
                notDisplayDestinationIds.forEach((destination_id) => {
                    if (destination_id < minDisplayDestinationId && prevDestination_ids.length < 3) {
                        prevDestination_ids.push(destination_id)
                    }
                })
                if (prevDestination_ids.length > 0) {
                    hideCurrentDisplayDestination()
                    displayDestination(prevDestination_ids)
                }
            }
        }
    });

    // property select
    $('li.location-item').click(function (ev) {
        let propertyIdInput = $('input#property-id')
        let locationItem = $('input#location')
        let selectPropertyId = this.dataset.locationId
        let selectPropertyName = this.innerText
        locationItem.val(selectPropertyName)
        propertyIdInput.val(selectPropertyId)
    });

    $('input.submit').click(function (ev) {
        debugger
        ev.preventDefault()
        let bookingForm = $('.booking-form')
        if (!bookingForm[0].checkValidity()) {
            bookingForm[0].reportValidity()
            return
        }
        let propertyId = $('input#property-id').val()
        if (!propertyId) {
            return
        }
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
            success: function (datas) {
                mainData = datas.data
                if (mainData.is_available) {
                    window.location.href = `/booking-step?property-detail-step&property-id=${propertyId}&check_in=${checkIn}&check_out=${checkOut}&no_guest=${noGuest}`
                } else {
                    $.jAlert({ //this is the normal usage
                        'title': 'Biệt thự đã được đặt. Xin vui lòng chọn ngày khác',
                        'content': 'Howdy',
                        'theme': 'green',
                        'size': 'xsm'
                    });

                }
            }
        })


    });

    $('#item-container > li').click(function (ev) {
        let destinationId = ev.currentTarget.dataset.destinationId
        window.location.href = `/destination/${destinationId}`
    })

})

