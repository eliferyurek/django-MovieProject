var update = document.getElementsByClassName('update-cart')

for(var i = 0; i < update.length; i++){
    update[i].addEventListener('click', function(){
        var movieID = this.dataset.product
        var action = this.dataset.action
        console.log('movieID', movieID, 'action', action)

        console.log('USER:', user)

        updateCustomerOrder(movieID, action)
    })
}

function updateCustomerOrder(movieID, action){
    var url = '/updatecart/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'movieID': movieID, 'action': action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data', data)
        location.reload()
    })
}
