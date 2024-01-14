$(document).ready(function () {
    function read_file(files) {
        return new Promise((resolve, reject) => {
            let reader = new FileReader();
            reader.onload = () => {
                resolve(reader.result);
            };
            reader.onerror = reject;
            reader.readAsDataURL(files);
        })
    }

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

    $('#dismiss-icon').click(function () {
        let applicantModal = $('.main-modal')
        applicantModal.fadeOut()
    });

    $('input#modal-submit-button').click(async function (ev) {
        ev.preventDefault()
        let applicantForm = $('#applicant-modal-form')
        if (!applicantForm[0].checkValidity()) {
            applicantForm[0].reportValidity()
            return
        }
        let jobId = $("select#job").find(":selected").val()
        let fullName = $("input#fullname").val()
        let birthday = $("input#birthday").val()
        let genderCode = $("select#gender").find(":selected").val()
        let phone = $("input#phone").val()
        let email = $("input#email").val()
        let joiningDate = $("input#joining-date").val()
        let certificateCode = $("select#certificate").val()
        let provinceCode = $("select#province").find(":selected").val()
        let certificateSubject = $("input#certificate-subject").val()
        let universityName = $("input#university-name").val()
        let expectedSalary = $("input#expected-salary").val()
        let jobExperienceCode = $("select#job-experience").find(":selected").val()
        let jobPosition = $("input#job-position").val()
        let socialMediaCode = $("select#social-media").find(":selected").val()
        let reader = await read_file($("input#cv-file")[0].files[0]);
        let cvFileBase64 = reader

        $.ajax({
            type: "POST",
            url: "/applicants/",
            data: {
                jobId: jobId,
                fullName: fullName,
                birthday: birthday,
                genderCode: genderCode,
                phone: phone,
                email: email,
                joiningDate: joiningDate,
                certificateCode: certificateCode,
                provinceCode: provinceCode,
                certificateSubject: certificateSubject,
                universityName: universityName,
                expectedSalary: expectedSalary,
                jobExperienceCode: jobExperienceCode,
                jobPosition: jobPosition,
                socialMediaCode: socialMediaCode,
                cvFileBase64: cvFileBase64,
            },
            success: function (data) {
                let button = $('#modal-submit-button')
                let successIcon = $('#success-message')
                button.hide()
                successIcon.css('display', 'flex')
            }, error: function (data) {
                console.log(data)
            }
        })
    });

})

function showApplicantPopup() {
    let applicantModal = $('.main-modal')
    applicantModal.fadeIn()
}