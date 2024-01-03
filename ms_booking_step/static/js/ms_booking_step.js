function setCheckinCheckoutVal(checkIn, checkOut, propertyId, noGuest) {
    let checkInSel = $('input#check-in')
    let checkOutSel = $('input#check-out')
    let propertyIdSel = $('input#property-id')
    let noGuestSel = $('input#no-guest')

    checkInSel.val(checkIn)
    checkOutSel.val(checkOut)
    propertyIdSel.val(propertyId)
    noGuestSel.val(noGuest)
}

function getNextState(stateSequence) {
    stateSequence = parseInt(stateSequence)
    let bsItems = $('.bs-item')
    let nextStateSequence = false
    for (let item = 0; item < bsItems.length; item++) {
        let itemStepSequence = parseInt(bsItems[`${item}`].dataset.stepSequence)
        if (itemStepSequence > stateSequence) {
            // nextStateSequence = bsItems[`${item}`]
            let nextStepSequenceDiv = `.bs-item[data-step-sequence='${itemStepSequence}']`
            nextStateSequence = $(nextStepSequenceDiv)
            break
        }
    }
    return nextStateSequence
}

function formatCurrency(price) {
    return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
}

function getCurrentStateSelector() {
    let activeBookingStep = $('.active-booking-step')
    let activeBookingStepSequence = activeBookingStep.length > 0 ? activeBookingStep[0].dataset.stepSequence : false
    return activeBookingStep

}

function resetTotalAmount(changePrice) {
    let totalAmountSel = $('#total-price')
    let currentTotalAmount = parseInt(totalAmountSel.text().replaceAll('.', ''))
    let result = currentTotalAmount + changePrice
    let formatResult = formatCurrency(result)
    totalAmountSel.text(formatResult)

}

function setDoneStep(stepSequence) {
    let hideStepDivSelector = `.step-sequence-title-${stepSequence}`
    let doneStepImgSelector = `.item-img-${stepSequence}`
    let bsTitleSelector = `.bs-title-${stepSequence}`

    let hideStepDiv = $(hideStepDivSelector)
    let doneStepImg = $(doneStepImgSelector)
    let bsTitle = $(bsTitleSelector)

    hideStepDiv.css('display', 'none')
    doneStepImg.fadeIn()
    bsTitle.css('color', 'black')

}

$(document).ready(function () {
    // $('.js_date_picker').datepicker({
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

    $('li.sd-property-pk').click(function (ev) {
        let propertyIdInput = $('input#property-id')
        let locationItem = $('input#location')
        let selectPropertyId = this.dataset.propertyId
        let selectPropertyName = this.innerText
        locationItem.val(selectPropertyName)
        propertyIdInput.val(selectPropertyId)
    });

    $('#booking-step-submit').click(function (ev) {
        ev.preventDefault()
        let bookingForm = $('#booking-form')
        if (!bookingForm[0].checkValidity()) {
            bookingForm[0].reportValidity()
            return
        }
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
            success: function (datas) {
                mainData = datas.data
                if (mainData.is_available) {
                    let propertyDetailDiv = $('div.bs-property-detail')
                    let formBookingContainer = $('.form-booking-container')
                    propertyDetailDiv.replaceWith(mainData.content);
                    let propertyDetailDiv2 = $('div.bs-property-detail')
                    let CurrentStateDiv = getCurrentStateSelector()
                    let CurrentState = CurrentStateDiv.length > 0 ? CurrentStateDiv[0].dataset.stepSequence : false
                    let NextState = getNextState(CurrentState)

                    CurrentStateDiv.removeClass('active-booking-step')
                    NextState.addClass('active-booking-step')
                    formBookingContainer.css('display', 'none')
                    propertyDetailDiv2.fadeIn(1000)
                    propertyDetailDiv2.css('display', 'flex')
                    propertyDetailDiv2.css('justify-content', 'center')
                    setCheckinCheckoutVal(checkIn, checkOut, propertyId, noGuest)
                    setDoneStep(CurrentState)
                } else {
                    let reservedBookingWarning = $('#reserved-booking-warning')
                    reservedBookingWarning.fadeIn()
                }
            }
        })

    });

})

function onClickReturnHomePage() {
    window.location.href = "/";
}

function onClickRedirectBookingDetail() {
    bookingId = parseInt($('#booking-id').val())
    window.location.href = `/booking/${bookingId}`;
}

function getOnBillExistedExtraService(serviceId) {
    let onBillserviceSelector = `.price-detail-info[data-bill-es-id=${serviceId}]`
    let onBillExtraService = $(onBillserviceSelector)
    return onBillExtraService
}


function onClickExtraService(ev) {
    let checkedInputs = $('.es-item-radio:checked')
    let notCheckedInputs = $(".es-item-radio:not(:checked)")
    let priceDetailDiv = $('div.price-detail')
    let nightValue = $('h5.night-value').text()

    notCheckedInputs.each(function () {
        let dataSets = this.dataset
        let isFullPackage = this
        let price = parseInt(dataSets.esPrice.split('.')[0]) * parseInt(nightValue)
        notCheckedId = dataSets.esId
        let onBillExtraService = getOnBillExistedExtraService(notCheckedId)
        if (onBillExtraService.length > 0) {
            // onBillExtraService.remove()
            onBillExtraService.hide('slow', function () {
                onBillExtraService.remove();
            })
            resetTotalAmount(parseInt(-price))

        }

    })

    checkedInputs.each(function () {
        let dataSets = this.dataset
        let price = parseInt(dataSets.esPrice.split('.')[0]) * parseInt(nightValue)
        let checkedId = dataSets.esId
        let existedOnBillES = getOnBillExistedExtraService(checkedId)
        if (!existedOnBillES.length) {
            let newDiv = `
                <div class="price-detail-info extra-service-added" data-bill-es-id="${checkedId}">
                    <p>${dataSets.esName}</p>
                    <p>${price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")}<span class="fb-price-currency">₫</span></p>
                </div>
        `
            priceDetailDiv.append(newDiv)
            // priceDetailDiv.slideDown('slow', function(){ priceDetailDiv.append(newDiv); })
            resetTotalAmount(parseInt(price))
        }
    });
}

function getActiveSliderDiv() {
    let currentActiveDiv = $('.active-div')
    return currentActiveDiv
}

function getCurrentMarginRightValue() {
    let activeDiv = getActiveSliderDiv()
    let marginRight = activeDiv.css('margin-right')
    return parseInt(marginRight.replace('px', ''))
}

function getMaxLengthNextMargin() {
    let totalSliderDiv = $('.div-size').length
    return -(totalSliderDiv * 900)
}

function getNextMargin() {
    let currentMargin = getCurrentMarginRightValue()
    let result = currentMargin <= getMaxLengthNextMargin() ? getMaxLengthNextMargin() : currentMargin - 900
    return result + 'px'
}

function getBackMargin() {
    let currentMargin = getCurrentMarginRightValue()
    let result = currentMargin == 0 ? 0 : currentMargin + 900
    return result + 'px'
}


function onClickNextImg() {
    let activeDiv = getActiveSliderDiv()
    let margin = getNextMargin()
    activeDiv.animate({'margin-right': margin}, 'fast')
}

function onClickBackImg() {
    let activeDiv = getActiveSliderDiv()
    let margin = getBackMargin()
    activeDiv.animate({'margin-right': margin}, 'fast')
}

function onClickExtraServiceStep(ev) {
    let checkIn = $('input#check-in').val()
    let checkOut = $('input#check-out').val()
    let propertyId = $('input#property-id').val()
    let totalAmount = $('p#total-amount').text()
    $.ajax({
        type: "GET",
        url: "/booking-step/extra-services",
        data: {
            checkIn: checkIn,
            checkOut: checkOut,
            propertyId: propertyId,
            totalAmount: totalAmount,
        },
        success: function (data) {
            let emptyDiv = $('.bs-extra-services')
            emptyDiv.replaceWith(data)
            let propertyDetail = $('.bs-property-detail')
            let extraServiceContainer = $('.bs-extra-services-container')
            let CurrentStateDiv = getCurrentStateSelector()
            let CurrentState = CurrentStateDiv.length > 0 ? CurrentStateDiv[0].dataset.stepSequence : false
            let NextState = getNextState(CurrentState)
            let totalAmountInput = $('input#total-amount')

            totalAmountInput.val(totalAmount)
            CurrentStateDiv.removeClass('active-booking-step')
            NextState.addClass('active-booking-step')
            propertyDetail.css('display', 'none')
            extraServiceContainer.fadeIn(1000)
            extraServiceContainer.css('display', 'flex')
            extraServiceContainer.css('justify-content', 'space-between')
            setDoneStep(CurrentState)
        }
    })
}

function getExtraServicesAdded() {
    let extraServicesAddedSelectors = $('.extra-service-added')
    let extraServiceIds = ''
    extraServicesAddedSelectors.each(function () {
        let esId = this.dataset.billEsId
        extraServiceIds = extraServiceIds.concat(',', esId);
    })
    return extraServiceIds
}

function getAppliedCoupons() {
    let appliedCouponsSelectors = $('.price-detail-info-coupon')
    let appliedCouponsIds = ''
    appliedCouponsSelectors.each(function () {
        let couponId = this.dataset.couponId
        appliedCouponsIds = appliedCouponsIds.concat(',', couponId);
    })
    return appliedCouponsIds
}

function onClickPaymentButton(ev) {
    let totalAmount = $('input#total-amount').val().replaceAll('.', '')
    let totalNights = $('input#total-nights').val()
    let esId = getExtraServicesAdded()
    $.ajax({
        type: "POST",
        url: "/booking-step/payment-confirm/",
        data: {
            'esId': esId,
            'totalAmount': totalAmount,
            'totalNights': totalNights,
        },
        success: function (data) {
            let emptyDiv = $('.bs-payment-confirm')
            emptyDiv.replaceWith(data)
            let extraServices = $('.bs-extra-services-container')
            let paymentConfirmationContainer = $('.bs-payment-confirmation-container')
            let CurrentStateDiv = getCurrentStateSelector()
            let CurrentState = CurrentStateDiv.length > 0 ? CurrentStateDiv[0].dataset.stepSequence : false
            let NextState = getNextState(CurrentState)

            CurrentStateDiv.removeClass('active-booking-step')
            NextState.addClass('active-booking-step')
            extraServices.css('display', 'none')
            paymentConfirmationContainer.fadeIn(1000)
            paymentConfirmationContainer.css('display', 'block')
            setDoneStep(CurrentState)
        }
    })
}

function onClickPaymentMethod(ev) {
    let qrCodeImgDiv = $('#qr-code-img')
    let checkedPaymentMethodCode = $('input[name="payment-method"]:checked').val();
    if (checkedPaymentMethodCode == 'qr_code') {
        qrCodeImgDiv.fadeIn()
        qrCodeImgDiv.css('display', 'flex')
        qrCodeImgDiv.css('justify-content', 'center')
    } else {
        qrCodeImgDiv.css('display', 'none')
    }

}

function onClickDeleteCoupon(dataset) {
    let couponId = dataset.couponId
    let couponDataValue = dataset.couponValue
    let voucherLine = `.price-detail-info-coupon[data-coupon-id=${couponId}]`
    let voucherLineDiv = $(voucherLine)
    voucherLineDiv.remove()

    let totalPriceDisplay = $('span#total-price')
    let totalPriceInput = $('input#final-pay')
    let totalPriceValue = parseInt(totalPriceInput.val().split('.')[0])
    let finalPrice = totalPriceValue + parseInt(couponDataValue)
    totalPriceDisplay.text(formatCurrency(finalPrice))
    totalPriceInput.val(finalPrice)
}

function onClickVoucherSubmit(ev) {
    let voucherCode = $('#payment-bill-voucher-code').val()
    $.ajax({
        type: "GET",
        url: "/coupons/get-coupon",
        data: {
            'voucherCode': voucherCode,
        },
        success: function (data) {
            console.log(data)
            let couponData = data.data
            let couponId = couponData.id

            let voucherLine = `.price-detail-info-coupon`
            let voucherLineDiv = $(voucherLine)
            if (couponData != {} && voucherLineDiv.length == 0) {
                let totalPriceDisplay = $('span#total-price')
                let totalPriceInput = $('input#final-pay')

                let totalPriceValue = parseInt(totalPriceInput.val().split('.')[0])
                let priceDetail = $('.price-detail')
                let couponDataValue = couponData.value
                let number = formatCurrency(couponDataValue);
                let couponDiv =
                    `<div class="price-detail-info price-detail-info-coupon" data-coupon-id="${couponId}">
                        <p>Giá thuê</p>
                        <p>-${number}<span class="fb-price-currency">₫</span>
                        <i data-coupon-id="${couponId}" data-coupon-value="${couponDataValue}" class="fa-solid fa-trash delete-applied-coupon" onclick="onClickDeleteCoupon(this.dataset)"></i>
                        </p>
                </div>`
                priceDetail.append(couponDiv)
                let finalPrice = totalPriceValue - couponDataValue
                totalPriceDisplay.text(formatCurrency(finalPrice))
                totalPriceInput.val(finalPrice)
            }
        }
    })
}

function onClickPaymentConfirmation() {
    let pccForm = $('#pcc-form')
    if (!pccForm[0].checkValidity()) {
        pccForm[0].reportValidity()
        return
    }
    let checkInVal = $('input#check-in').val()
    let checkOutVal = $('input#check-out').val()
    let propertyIdVal = $('input#property-id').val()
    let noGuestVal = $('input#no-guest').val()
    let totalAmountVal = $('input#final-pay').val()
    let fullName = $('input#fullname').val()
    let email = $('input#email').val()
    let phone = $('input#phone').val()
    let customerRequest = $('textarea#customer-request').val()
    let PaymentMethodCode = $('input[name="payment-method"]:checked').val();
    let appliedVoucherIds = getAppliedCoupons()

    let esId = getExtraServicesAdded()
    let submitPaymentButton = $('#submit-payment-button')
    let loadingDiv = $('#loading')
    submitPaymentButton.replaceWith(loadingDiv)
    loadingDiv.css('display', 'flex')
    $.ajax({
        type: "POST",
        url: "/booking-step/booking-confirm/",
        data: {
            'check_in': checkInVal,
            'check_out': checkOutVal,
            'property_id': propertyIdVal,
            'no_guest': noGuestVal,
            'total_amount': totalAmountVal,
            'customer_name': fullName,
            'customer_email': email,
            'customer_phone': phone,
            'customer_request': customerRequest,
            'payment_method_code': PaymentMethodCode,
            'es_ids': esId,
            'appliedVoucherIds': appliedVoucherIds,
        },
        success: function (data) {
            let emptyDiv = $('.bs-booking-confirm-container')
            emptyDiv.replaceWith(data)
            let paymentConfirmationContainer = $('.bs-payment-confirmation-container')
            let bookingConfirmationContainer = $('.bs-booking-confirm-container')
            let CurrentStateDiv = getCurrentStateSelector()
            let CurrentState = CurrentStateDiv.length > 0 ? CurrentStateDiv[0].dataset.stepSequence : false
            let NextState = getNextState(CurrentState)

            CurrentStateDiv.removeClass('active-booking-step')
            NextState.addClass('active-booking-step')
            paymentConfirmationContainer.css('display', 'none')
            bookingConfirmationContainer.css('display', 'flex')
            bookingConfirmationContainer.css('justify-content', 'center')
            setDoneStep(CurrentState)
            loadingDiv.fadeOut()
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest)
            console.log(textStatus)
            console.log(errorThrown)
            reservedBookingWarningFinal = $('.reservedBookingWarningFinal')
            reservedBookingWarningFinal.fadeIn()
            loadingDiv.fadeOut()
        }
    })
}



