document.addEventListener('DOMContentLoaded', () => {
    var socket = io.connect('http://' + document.domain + ':' + location.port)

    socket.on('connect', () => {
        console.log('connected')
        socket.emit('sum', {numbers:[1,2]})
    })

    socket.on('disconnect', () => {
        console.log('disconnected')
    })

    socket.on('sum_result', (data) => {
        console.log(data)
    })

    socket.on('message', data => {
        console.log(`Message received: ${data}`)
    })

    socket.on('some-event', data => {
        console.log(data)
    })
})

// var socket;
// connectToSocket();

// function connectToSocket(){
//   socket = io.connect('http://' + document.domain + ':' + location.port);
//   socket.on('connect', function() {
//       socket.send('I am connected!');
//   });

//   socket.on('message', data => {
//     console.log(`Message received: ${data}`)
// });
  
// }
