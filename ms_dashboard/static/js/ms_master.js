$(document).ready(function () {

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