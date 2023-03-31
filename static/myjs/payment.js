function payment() {
    var paymentmethod = 'online';
    // alert(paymentmethod);
    if (paymentmethod == "online") {
        // e.preventDefault();
        var amount = document.getElementById('grandtotal2').innerText * 100;
        // alert(amount)
        // alert(typeof  amount)
        var options = {
            "key": "rzp_test_dRWiKHS7zr2Gki",
            "amount": amount,
            "name": "Restabook",
            "description": "",
            "image": "",
            "handler": function (response) {
                //alert(response.razorpay_payment_id);
                if (response.razorpay_payment_id == "") {
                    alert('Failed');
                    // window.location.href = "failedPayment";
                } else {
                    var httpreg = new XMLHttpRequest();
                    httpreg.onreadystatechange = function () {
                        if (this.status == 200 && this.readyState == 4) {
                            var output = JSON.parse(this.response);
                            alert(output['status']);
                            if (output['status'] == true) {
                                location.href = 'thankspage/' + output['orderid']
                            }
                        }
                    };
                    httpreg.open("POST", "confirmOrder", true);
                    httpreg.send();
                }
            },
            "prefill": {
                "name": "",
                "email": document.getElementById('email').innerText,
                "contact": document.getElementById('mobile').innerText,
            },
            "notes": {
                "address": ""
            },
            "theme": {
                "color": "#282424"
            }
        };
        var rzp1 = new Razorpay(options);
        rzp1.open();
    } else {
        // var controls = document.getElementById("mycheckout").elements;
        // var formdata = new FormData();
        // for (var i = 0; i < controls.length; i++) {
        //     if (controls[i].type == "file") {
        //         formdata.append(controls[i].name, controls[i].files[0]);
        //     } else if (controls[i].type == "radio") {
        //         formdata.append(controls[i].name, $("input[name=" + controls[i].name + "]:checked").val());
        //     } else {
        //         formdata.append(controls[i].name, controls[i].value);
        //     }
        // }
        var httpreg = new XMLHttpRequest();
        httpreg.onreadystatechange = function () {
            if (this.status == 200 && this.readyState == 4) {
                var output = JSON.parse(this.response);
                alert(output['status']);
                if (output['status'] == true) {
                    location.href = 'thankspage/' + output['orderid']
                }
            }
        };
        httpreg.open("POST", "confirmOrder", true);
        httpreg.send();
    }

}