$(document).ready(function () {
    $('.changePasswordModalSubmitButton').click(function (ev) {
        let changePasswordModalForm = $('.changePasswordModalForm')
        if (!changePasswordModalForm[0].checkValidity()) {
            changePasswordModalForm[0].reportValidity()
            return
        }
        let userId = $('select#user-id').val()
        let newPassword = $('input#new-password').val()
        let confirmPassword = $('input#confirm-password').val()
        if (newPassword != confirmPassword) {
            let changePasswordModalFormWarning = $('.changePasswordModalFormWarning')
            changePasswordModalFormWarning.fadeIn()
            return
        }
        $.ajax({
            type: "POST",
            url: "/partners/change-password/",
            data: {
                'userId': userId,
                'newPassword': newPassword,
            },
            success: function (data) {
                window.location.href = "/partners"

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                console.log(XMLHttpRequest)
                console.log(textStatus)
                console.log(errorThrown)
            }
        })
    })

    $('.inactiveAccountModalSubmitButton').click(function (ev) {
        let inactiveAccountModalForm = $('.inactiveAccountModal')
        if (!inactiveAccountModalForm[0].checkValidity()) {
            inactiveAccountModalForm[0].reportValidity()
            return
        }
        let userId = $('select#user-id-1').val()
        let type = $('select#type').val()
        $.ajax({
            type: "POST",
            url: "/partners/inactive-account/",
            data: {
                'userId': userId,
                'type': type,
            },
            success: function (data) {
                window.location.href = "/partners"

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                console.log(XMLHttpRequest)
                console.log(textStatus)
                console.log(errorThrown)
            }
        })
    })

})
