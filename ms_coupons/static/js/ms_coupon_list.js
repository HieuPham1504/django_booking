$(document).ready(function () {
    $('.createCouponModalSubmitButton').click(function (ev) {
        let createCouponModalForm = $('.createCouponModalForm')
        if (!createCouponModalForm[0].checkValidity()) {
            createCouponModalForm[0].reportValidity()
            return
        }
        let couponName = $('input#coupon-name').val()
        let couponValue = $('input#coupon-value').val()
        let dateStart = $('input#date-start').val()
        let dateEnd = $('input#date-end').val()

        if (dateStart > dateEnd) {
            let wrongDateWarning = $('.wrongDateWarning')
            wrongDateWarning.fadeIn()
            return
        }
        $.ajax({
            type: "POST",
            url: "/coupons/create/",
            data: {
                'couponName': couponName,
                'dateStart': dateStart,
                'dateEnd': dateEnd,
                'couponValue': couponValue,
            },
            success: function (data) {
                window.location.href = "/coupons"

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                console.log(XMLHttpRequest)
                console.log(textStatus)
                console.log(errorThrown)
            }
        })
    })

    $('.deleteCouponModalSubmitButton').click(function (ev) {
        let checkedCheckboxes =  Array.from($('input.coupon-checkbox-item:checked'));
        let checkedRowIds = ''
        checkedCheckboxes.forEach((input) => {
            checkedRowIds = checkedRowIds.concat(',', input.dataset.couponId);
        });
        $.ajax({
            type: "POST",
            url: "/coupons/delete/",
            data: {
                'row_ids': checkedRowIds,
            },
            success: function (data) {
                window.location.href = "/coupons"

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                console.log(XMLHttpRequest)
                console.log(textStatus)
                console.log(errorThrown)
            }
        })
    })

    function displayDeleteButton() {
        let checkedCheckboxes = $('input.coupon-checkbox-item:checked').length;
        deleteCuponBtn = $('button.deleteCoupon')
        if (checkedCheckboxes > 0) {
            deleteCuponBtn.fadeIn()
        } else {
            deleteCuponBtn.fadeOut()
        }
    }

    $('.coupon-checkbox-all').click(function (ev) {
        isChecked = this.checked
        couponCheckboxItems = $('.coupon-checkbox-item')
        if (isChecked) {
            couponCheckboxItems.prop('checked', true);
            displayDeleteButton()
        } else {
            couponCheckboxItems.prop('checked', false);
            displayDeleteButton()
        }

    })

    $('.coupon-checkbox-item').click(function (ev) {
        isChecked = this.checked
        if (!isChecked) {
            couponCheckboxAll = $('.coupon-checkbox-all')
            couponCheckboxAll.prop('checked', false);
            displayDeleteButton()
        } else {
            displayDeleteButton()
        }

    })

})