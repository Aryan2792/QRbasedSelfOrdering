window.onload = getCartDetails();

function getCartDetails() {
    var httpreg = new XMLHttpRequest();
    httpreg.onreadystatechange = function () {
        if (this.status == 200 && this.readyState == 4) {
            var output = JSON.parse(this.response);
            // console.log(output)
            makeCartTable(output['cart'])
            document.getElementById('grandtotal2').innerText = output['gtotal']
            document.getElementById('grandtotal1').innerText = output['gtotal']
        }
    };
    httpreg.open("POST", "getCartDetails", true);
    httpreg.send();
}


function makeCartTable(cart) {
    s = ""
    for (var i = 0; i < cart.length; i++) {
        s += `<tr>
                                        <td class="hidden-xs">
                                            <a href="#"><img src="/static/media/${cart[i].photo}" alt=""
                                                             class="respimg"></a>
                                        </td>
                                        <td>
                                            <h5 class="product-name">${cart[i].item}</h5>
                                        </td>
                                        <td class="hidden-xs">
                                            <h5 class="order-money">₹${cart[i].price}</h5>
                                        </td>
                                        <td>
                                            <input type="number" onchange="changeQuantity(this, ${cart[i].id})" name="quantity" id="quantity" value="${cart[i].quantity}" max="50"
                                                   min="1"
                                                   class="order-count">
                                        </td>
                                        <td>
                                            <h5 class="order-money">₹${cart[i].total}</h5>
                                        </td>
                                        <td class="pr-remove">
                                            <a href="javascript:void(0)" title="Remove" onclick="removeCart(${cart[i].id})"><i class="fal fa-times"></i></a>
                                        </td>
                                    </tr>`
    }
    document.getElementById('mycart').innerHTML = s;
}

function removeCart(id) {
    alert(id)
    var httpreg = new XMLHttpRequest();
    httpreg.onreadystatechange = function () {
        if (this.status == 200 && this.readyState == 4) {
            var output = this.response
            if(output=='success'){
                getCartDetails()
            }
        }
    };
    httpreg.open("GET", "removeCart/"+id, true);
    httpreg.send();
}

function changeQuantity(obj, id) {
    var httpreg = new XMLHttpRequest();
    httpreg.onreadystatechange = function () {
        if (this.status == 200 && this.readyState == 4) {
            var output = this.response
            if(output=='success'){
                getCartDetails()
            }
        }
    };
    httpreg.open("GET", "changeQuantity/"+id+'/'+obj.value, true);
    httpreg.send();
}