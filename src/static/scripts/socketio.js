document.addEventListener('DOMContentLoaded', () => {
    var socket = io.connect('http://' + document.domain + ':' + location.port)

    socket.on('connect', () => {
        console.log('connected to server')
        //one can substitute 'send' with 'emit' but emit is preffered
        //since it can send both string and objects while send only sends strings
        socket.send('I am connected')
        // socket.emit('sum', {numbers:[1,2]})
    })

    socket.on('message', data => {
        const p = document.createElement('p')
        const user = document.createElement('span')
        const br = document.createElement('br')
        user.innerHTML = data.username
        p.innerHTML = user.outerHTML+ br.outerHTML + data.msg + br.outerHTML
        document.querySelector('#display-message-section').append(p)
        // console.log(`Message received: ${data}`)
    })

    socket.on('calling', data => {
        console.log(data)
    })

    socket.on('disconnect', () => {
        console.log('disconnected from server')
        socket.emit('client has been disconnected')
    })

    // send message
    document.querySelector('#send_message').onclick = () =>{
        socket.send({'msg': document.querySelector('#user_message').value,
        'username': username})
    }

})


