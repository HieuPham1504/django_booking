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