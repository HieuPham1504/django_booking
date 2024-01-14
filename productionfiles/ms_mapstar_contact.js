$(document).ready(function () {
    $('input.form-submit').click(function (ev) {
        ev.preventDefault()
        let contactForm = $('#contact-form')
        if (!contactForm[0].checkValidity()) {
            contactForm[0].reportValidity()
            return
        }
        let fullName = $('input#fullname').val()
        let phoneNumber = $('input#phone-number').val()
        let email = $('input#email').val()
        let requestForm = $('#request').val()
        $.ajax({
            type: "POST",
            url: "/mapstar-contact/create-contact-request/",
            data: {
                fullName: fullName,
                phoneNumber: phoneNumber,
                email: email,
                request: requestForm,
            },
            success: function (data) {
                let message = $('p.response-message-value')
                let messageDiv = $('div.response-message')
                message.text(data);
                messageDiv.removeClass('inactive-div')
            }
        })
    });
})