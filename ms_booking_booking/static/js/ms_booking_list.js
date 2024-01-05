$(document).ready(function () {
    $('#date-start.js_date_picker').daterangepicker({
            opens: 'right',
            language: 'vi',
            autoUpdateInput: false,
            startDate: new Date(),
            minDate: new Date(),
            function(start, end, label) {
                debugger
                $(this).val(start.format("DD/MM/YYYY"));
            },
            locale: {
                "format":
                    'DD/MM/YYYY',
                "applyLabel":
                    "Chọn",
                "cancelLabel":
                    "Hủy",
                "daysOfWeek":
                    [
                        "CN",
                        "T2",
                        "T3",
                        "T4",
                        "T5",
                        "T6",
                        "T7"
                    ],
                "monthNames":
                    [
                        "Tháng 1",
                        "Tháng 2",
                        "Tháng 3",
                        "Tháng 4",
                        "Tháng 5",
                        "Tháng 6",
                        "Tháng 7",
                        "Tháng 8",
                        "Tháng 9",
                        "Tháng 10",
                        "Tháng 11",
                        "Tháng 12"
                    ],
            }
            ,
        },

        function (start, end, label) {
            $('.js_date_picker#date-start').val(start.format('DD/MM/YYYY'))
            $('.js_date_picker#date-end').val(end.format('DD/MM/YYYY'))
        }

        ,
        $('#date-start.js_date_picker').on('apply.daterangepicker', function (ev, picker) {
            $(this).val(picker.startDate.format('DD/MM/YYYY')); // set value for this
            // anything else you want to do
        })
    );

    $('#date-end.js_date_picker').daterangepicker({
            opens: 'left',
            language: 'vi',
            autoUpdateInput: false,
            startDate: new Date(),
            minDate: new Date(),
            function(start, end, label) {
                debugger
                $(this).val(start.format("DD/MM/YYYY"));
            },
            locale: {
                "format":
                    'DD/MM/YYYY',
                "applyLabel":
                    "Chọn",
                "cancelLabel":
                    "Hủy",
                "daysOfWeek":
                    [
                        "CN",
                        "T2",
                        "T3",
                        "T4",
                        "T5",
                        "T6",
                        "T7"
                    ],
                "monthNames":
                    [
                        "Tháng 1",
                        "Tháng 2",
                        "Tháng 3",
                        "Tháng 4",
                        "Tháng 5",
                        "Tháng 6",
                        "Tháng 7",
                        "Tháng 8",
                        "Tháng 9",
                        "Tháng 10",
                        "Tháng 11",
                        "Tháng 12"
                    ],
            }
            ,
        },

        function (start, end, label) {
            $('.js_date_picker#date-start').val(start.format('DD/MM/YYYY'))
            $('.js_date_picker#date-end').val(end.format('DD/MM/YYYY'))
        },
        $('#date-end.js_date_picker').on('apply.daterangepicker', function (ev, picker) {
            $(this).val(picker.endDate.format('DD/MM/YYYY')); // set value for this
            // anything else you want to do
        })
    );

    $('#checkin.js_date_picker').daterangepicker({
            opens: 'right',
            drops: 'up',
            language: 'vi',
            autoUpdateInput: false,
            startDate: new Date(),
            minDate: new Date(),
            function(start, end, label) {
                $(this).val(start.format("DD/MM/YYYY"));
            },
            locale: {
                "format":
                    'DD/MM/YYYY',
                "applyLabel":
                    "Chọn",
                "cancelLabel":
                    "Hủy",
                "daysOfWeek":
                    [
                        "CN",
                        "T2",
                        "T3",
                        "T4",
                        "T5",
                        "T6",
                        "T7"
                    ],
                "monthNames":
                    [
                        "Tháng 1",
                        "Tháng 2",
                        "Tháng 3",
                        "Tháng 4",
                        "Tháng 5",
                        "Tháng 6",
                        "Tháng 7",
                        "Tháng 8",
                        "Tháng 9",
                        "Tháng 10",
                        "Tháng 11",
                        "Tháng 12"
                    ],
            }
            ,
        },

        function (start, end, label) {
            $('.js_date_picker#checkin').val(start.format('DD/MM/YYYY'))
            $('.js_date_picker#checkout').val(end.format('DD/MM/YYYY'))
            $.ajax({
                type: "GET",
                url: "/property/total-amount",
                data: {
                    'checkin': start.format('DD/MM/YYYY'),
                    'checkout': end.format('DD/MM/YYYY'),
                    'propertyId': parseInt($('#booking-property').val()),
                },
                success: function (data) {
                    let totalAmount = $('#total-amount')
                    totalAmount.val(formatCurrency(data.total_amount))
                }
            })
        }

        ,
        $('#checkin.js_date_picker').on('apply.daterangepicker', function (ev, picker) {
            $(this).val(picker.startDate.format('DD/MM/YYYY')); // set value for this
            $.ajax({
                type: "GET",
                url: "/property/total-amount",
                data: {
                    'checkin': picker.startDate.format('DD/MM/YYYY'),
                    'checkout': picker.endDate.format('DD/MM/YYYY'),
                    'propertyId': parseInt($('#booking-property').val()),
                },
                success: function (data) {
                    let totalAmount = $('#total-amount')
                    totalAmount.val(formatCurrency(data.total_amount))
                }
            })
        })
    );

    $('#checkout.js_date_picker').daterangepicker({
            opens: 'left',
            drops: 'up',
            language: 'vi',
            autoUpdateInput: false,
            startDate: new Date(),
            minDate: new Date(),
            function(start, end, label) {
                $(this).val(start.format("DD/MM/YYYY"));
            },
            locale: {
                "format":
                    'DD/MM/YYYY',
                "applyLabel":
                    "Chọn",
                "cancelLabel":
                    "Hủy",
                "daysOfWeek":
                    [
                        "CN",
                        "T2",
                        "T3",
                        "T4",
                        "T5",
                        "T6",
                        "T7"
                    ],
                "monthNames":
                    [
                        "Tháng 1",
                        "Tháng 2",
                        "Tháng 3",
                        "Tháng 4",
                        "Tháng 5",
                        "Tháng 6",
                        "Tháng 7",
                        "Tháng 8",
                        "Tháng 9",
                        "Tháng 10",
                        "Tháng 11",
                        "Tháng 12"
                    ],
            }
            ,
        },

        function (start, end, label) {
            $('.js_date_picker#checkin').val(start.format('DD/MM/YYYY'))
            $('.js_date_picker#checkout').val(end.format('DD/MM/YYYY'))
            $.ajax({
                type: "GET",
                url: "/property/total-amount",
                data: {
                    'checkin': start.format('DD/MM/YYYY'),
                    'checkout': end.format('DD/MM/YYYY'),
                    'propertyId': parseInt($('#booking-property').val()),
                },
                success: function (data) {
                    let totalAmount = $('#total-amount')
                    totalAmount.val(formatCurrency(data.total_amount))
                }
            })
        },
        $('#checkout.js_date_picker').on('apply.daterangepicker', function (ev, picker) {
            $(this).val(picker.endDate.format('DD/MM/YYYY')); // set value for this
            $.ajax({
                type: "GET",
                url: "/property/total-amount",
                data: {
                    'checkin': picker.startDate.format('DD/MM/YYYY'),
                    'checkout': picker.endDate.format('DD/MM/YYYY'),
                    'propertyId': parseInt($('#booking-property').val()),
                },
                success: function (data) {
                    let totalAmount = $('#total-amount')
                    totalAmount.val(formatCurrency(data.total_amount))
                }
            })
        })
    );

    $('#booking-property').change(function (ev) {
        debugger
        currentTarget = ev.currentTarget
        let propertyId = parseInt(currentTarget.value)
        $.ajax({
            type: "GET",
            url: "/property/total-amount",
            data: {
                'checkin': $('#checkin').val(),
                'checkout': $('#checkout').val(),
                'propertyId': propertyId,
            },
            success: function (data) {
                let totalAmount = $('#total-amount')
                totalAmount.val(formatCurrency(data.total_amount))
            }
        })
    })

    $('#total-amount').keyup(function (ev) {
        debugger
        currentTarget = ev.currentTarget
        let currentAmount = currentTarget.value
        let finalAmount = formatCurrency(currentAmount.replaceAll('.', ''))
        currentTarget.value = finalAmount
    })

    $('.cancelBookingModalSubmitButton').click(function (ev) {
        let checkedCheckboxes = Array.from($('input.booking-checkbox-item:checked'));
        let cancelReason = $('#cancel-reason').val()
        let checkedRowIds = ''
        checkedCheckboxes.forEach((input) => {
            checkedRowIds = checkedRowIds.concat(',', input.dataset.bookingId);
        });

        let cancelBookingModalSubmitButton = $('.cancelBookingModalSubmitButton')
        let cancelBookingLoading = $('.cancelBookingLoading')
        cancelBookingModalSubmitButton.css('display', 'none')
        cancelBookingLoading.fadeIn()

        $.ajax({
            type: "POST",
            url: "/booking/cancel/",
            data: {
                'row_ids': checkedRowIds,
                'cancelReason': cancelReason,
            },
            success: function (data) {
                window.location.href = "/booking"
                cancelBookingLoading.css('display', 'none')
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                cancelBookingLoading.css('display', 'none')
                cancelBookingModalSubmitButton.fadeIn()
                console.log(XMLHttpRequest)
                console.log(textStatus)
                console.log(errorThrown)
            }
        })
    })

    $('.createBookingModalSubmitButton').click(function (ev) {
        debugger
        let customerName = $('#customer-name').val()
        let customerPhone = $('#customer-phone').val()
        let customerEmail = $('#customer-email').val()
        let checkin = $('#checkin').val()
        let checkout = $('#checkout').val()
        let propertyId = $('#booking-property').val()
        let bookingSourceId = $('#booking-source').val()
        let noGuest = $('#no-guest').val()
        let paymentMethodId = $('#payment-method').val()

        let totalAmount = parseInt($('#total-amount').val().replaceAll('.', ''))
        let createBookingModalSubmitButton = $('.createBookingModalSubmitButton')
        let createBookingLoading = $('.createBookingLoading')
        createBookingLoading.fadeIn()
        createBookingModalSubmitButton.css('display', 'none')
        $.ajax({
            type: "POST",
            url: "/booking/create/",
            data: {
                'customerName': customerName,
                'customerPhone': customerPhone,
                'customerEmail': customerEmail,
                'checkin': checkin,
                'checkout': checkout,
                'noGuest': noGuest,
                'propertyId': propertyId,
                'bookingSourceId': bookingSourceId,
                'paymentMethodId': paymentMethodId,
                'totalAmount': totalAmount,
            },
            success: function (data) {
                window.location.href = "/booking"
                createBookingLoading.css('display', 'none')
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                createBookingLoading.css('display', 'none')
                createBookingModalSubmitButton.fadeIn()
                createBookingWarning = $('.createBookingWarning')
                createBookingWarning.text(XMLHttpRequest.responseText)
                createBookingWarning.fadeIn()
                console.log(XMLHttpRequest)
                console.log(textStatus)
                console.log(errorThrown)
            }
        })
    })

    $('.confirmBookingModalSubmitButton').click(function (ev) {
        let checkedCheckboxes = Array.from($('input.booking-checkbox-item:checked'));
        let checkedRowIds = ''
        checkedCheckboxes.forEach((input) => {
            checkedRowIds = checkedRowIds.concat(',', input.dataset.bookingId);
        });

        let confirmBookingModalSubmitButton = $('.confirmBookingModalSubmitButton')
        let confirmBookingLoading = $('.confirmBookingLoading')
        confirmBookingModalSubmitButton.css('display', 'none')
        confirmBookingLoading.fadeIn()
        $.ajax({
            type: "POST",
            url: "/booking/done/",
            data: {
                'row_ids': checkedRowIds,
            },
            success: function (data) {
                window.location.href = "/booking"
                confirmBookingLoading.css('display', 'none')
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                confirmBookingLoading.css('display', 'none')
                confirmBookingModalSubmitButton.fadeIn()
                console.log(XMLHttpRequest)
                console.log(textStatus)
                console.log(errorThrown)
            }
        })
    })


    function displayBookingButton() {
        let checkedCheckboxes = $('input.booking-checkbox-item:checked').length;
        let cancelBookingBtn = $('button.buttonCancelBooking')
        let confirmBookingBtn = $('button.buttonConfirmBooking')
        if (checkedCheckboxes > 0) {
            cancelBookingBtn.fadeIn()
            confirmBookingBtn.fadeIn()
        } else {
            cancelBookingBtn.fadeOut()
            confirmBookingBtn.fadeOut()
        }
    }

    $('.booking-checkbox-all').click(function (ev) {
        isChecked = this.checked
        let bookingCheckboxItems = $('.booking-checkbox-item')
        if (isChecked) {
            bookingCheckboxItems.prop('checked', true);
            displayBookingButton()
        } else {
            bookingCheckboxItems.prop('checked', false);
            displayBookingButton()
        }

    })

    $('.booking-checkbox-item').click(function (ev) {
        isChecked = this.checked
        if (!isChecked) {
            let bookingCheckboxAll = $('.booking-checkbox-all')
            bookingCheckboxAll.prop('checked', false);
            displayBookingButton()
        } else {
            displayBookingButton()
        }

    })

    function formatCurrency(price) {
        return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
    }

    $('.booking-detail-row > td').click(function (ev) {
        let currentRow = ev.currentTarget.parentElement.dataset
        let bookingId = parseInt(currentRow.bookingId)
        window.location.href = `/booking/${bookingId}`
    })

    $('#filter-type').change(function () {
        let data = $(this).val();
        let dateInput = $('.date-input')
        let bookingCodeInput = $('.booking-code-input')
        let partnerTypeInput = $('.partner-type-input')
        let propertyInput = $('.property-input')
        let partnerTypeIndividualValue = $('.partner-type-individual-value')
        let partnerTypeAgencyValue = $('.partner-type-agency-value')
        // alert(data);
        filterDate = ['check_in', 'check_out']
        if (filterDate.includes(data)) {
            bookingCodeInput.css('display', 'none')
            propertyInput.css('display', 'none')
            partnerTypeInput.css('display', 'none')
            partnerTypeIndividualValue.css('display', 'none')
            partnerTypeAgencyValue.css('display', 'none')
            dateInput.fadeIn()
        } else if (data == 'booking_code') {
            dateInput.css('display', 'none')
            partnerTypeInput.css('display', 'none')
            bookingCodeInput.fadeIn()
            partnerTypeIndividualValue.css('display', 'none')
            partnerTypeAgencyValue.css('display', 'none')
            propertyInput.css('display', 'none')
        } else if (data == 'partner_type') {
            dateInput.css('display', 'none')
            propertyInput.css('display', 'none')
            bookingCodeInput.css('display', 'none')
            partnerTypeInput.fadeIn()

        } else if (data == 'property') {
            dateInput.css('display', 'none')
            partnerTypeInput.css('display', 'none')
            partnerTypeIndividualValue.css('display', 'none')
            partnerTypeAgencyValue.css('display', 'none')
            propertyInput.fadeIn()
        }
    });

    $('#partner-type').change(function () {
        debugger
        let data = $(this).val();
        let partnerTypeIndividualValue = $('.partner-type-individual-value')
        let partnerTypeAgencyValue = $('.partner-type-agency-value')
        if (data == 'individual') {
            partnerTypeAgencyValue.css('display', 'none')
            partnerTypeIndividualValue.fadeIn()
        } else if (data == 'agency') {
            partnerTypeIndividualValue.css('display', 'none')
            partnerTypeAgencyValue.fadeIn()
        } else {
            partnerTypeAgencyValue.css('display', 'none')
            partnerTypeIndividualValue.css('display', 'none')
        }
    })
})