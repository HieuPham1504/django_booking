$(document).ready(function () {
    // $(function () {
    //     let isMobile = (window.matchMedia("(max-width: 767px)").matches) ? true : false;
    //     $('input.js_date_picker').daterangepicker({
    //         opens: 'left',
    //         singleDatePicker: isMobile,
    //     }, function (start, end, label) {
    //         console.log("Mobile date range picker");
    //     });
    // });

    // $('.js_date_picker_mobile').datepicker({
    //     dateFormat: 'dd/mm/yy',
    //     useCurrent: false,
    //     keepOpen: false,
    //     icons: {
    //         time: 'fa fa-clock-o',
    //         date: 'fa fa-calendar',
    //         up: 'fa fa-chevron-up',
    //         down: 'fa fa-chevron-down',
    //         previous: 'fa fa-chevron-left',
    //         next: 'fa fa-chevron-right',
    //         today: 'fa fa-calendar-check-o',
    //         clear: 'fa fa-trash',
    //         close: 'fa fa-check primary',
    //     },
    //     buttons: {
    //         showToday: true,
    //         showClear: false,
    //         showClose: true,
    //     },
    // });

    let isMobile = (window.matchMedia("(max-width: 767px)").matches) ? true : false;

    $('#checkin.js_date_picker').daterangepicker({
            opens: 'right',
            language: 'vi',
            autoUpdateInput: false,
            startDate: new Date(),
            minDate: new Date(),
            singleDatePicker: isMobile,
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
            if (isMobile) {
                $('.js_date_picker#checkin').val(start.format('DD/MM/YYYY'))
            } else {
                $('.js_date_picker#checkin').val(start.format('DD/MM/YYYY'))
                $('.js_date_picker#checkout').val(end.format('DD/MM/YYYY'))
            }
        }

        ,
        $('#checkin.js_date_picker').on('apply.daterangepicker', function (ev, picker) {
            $(this).val(picker.startDate.format('DD/MM/YYYY')); // set value for this
            // anything else you want to do
        })
    );


    $('#checkout.js_date_picker').daterangepicker({
            opens: 'left',
            language: 'vi',
            autoUpdateInput: false,
            startDate: new Date(),
            minDate: new Date(),
            singleDatePicker: isMobile,
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
            if (isMobile) {
                $('.js_date_picker#checkout').val(end.format('DD/MM/YYYY'))
            } else {
                $('.js_date_picker#checkin').val(start.format('DD/MM/YYYY'))
                $('.js_date_picker#checkout').val(end.format('DD/MM/YYYY'))
            }
        },
        $('#checkout.js_date_picker').on('apply.daterangepicker', function (ev, picker) {
            $(this).val(picker.endDate.format('DD/MM/YYYY')); // set value for this
            // anything else you want to do
        })
    );


    window.addEventListener('click', ({target}) => {
        const locationInput = target.closest('#location');
        const locationSuggest = $('.location-suggest');
        const ourDestinationH2 = $('.our-destinations h2');
        const clickedOnClosedPopup = !locationInput

        if (clickedOnClosedPopup && locationSuggest) {
            locationSuggest.removeClass('active');
            ourDestinationH2.css('margin-top', '0')
        }
    });

    $('input#location').click(function () {
        const ourDestinationH2 = $('.our-destinations h2');

        $('.location-suggest').toggleClass('active')
        ourDestinationH2.css('margin-top', '80px')
    });

    $('#menuToggle').click(function () {
        $('#menu').toggleClass('active')
    });

    $("#logo").click(function () {
        window.location.href = "/";
    });

    var lastScrollTop;

    navbar = document.getElementById('navbar'); // Get The NavBar

    window.addEventListener('scroll', function () {
        //on every scroll this funtion will be called

        var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        //This line will get the location on scroll

        if (scrollTop > lastScrollTop) { //if it will be greater than the previous
            navbar.style.top = '-100px';
            //set the value to the negetive of height of navbar
        } else {
            navbar.style.top = '0';
        }

        lastScrollTop = scrollTop; //New Position Stored
    });

    $(".slider-container").hover(function () {
        $("#next img").css('display', 'block');
        $("#previous img").css('display', 'block');
    }, function () {
        $("#next img").css('display', 'none');
        $("#previous img").css('display', 'none');
    });


})