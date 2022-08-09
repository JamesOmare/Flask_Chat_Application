document.addEventListener('DOMContentLoaded', () => {
    var socket = io.connect('http://' + document.domain + ':' + location.port)
    
    //default room 
    let room = 'Music'
    join_room('Music')

    socket.on('connect', () => {
        console.log('connected to server')
        //one can substitute 'send' with 'emit' but emit is preffered
        //since it can send both string and objects while send only sends strings
        socket.send('I am connected')
        // socket.emit('sum', {numbers:[1,2]})
    })

    //Display incoming messages
    socket.on('message', data => {
        const p = document.createElement('p')
        const user = document.createElement('span')
        const time_stamp = document.createElement('span')
        const br = document.createElement('br')

        if(data.username){
            user.innerHTML = data.username
        time_stamp.innerHTML = data.timestamp
        p.innerHTML = user.outerHTML+ br.outerHTML + data.msg + br.outerHTML + time_stamp.outerHTML
        document.querySelector('#display-message-section').append(p)
        } 

        else{
            prompt_message(data.msg)
        }
        
        
    })


    socket.on('disconnect', () => {
        console.log('disconnected from server')
        socket.emit('client has been disconnected')
    })

    // send message
    document.querySelector('#send_message').onclick = () =>{
        socket.emit('message', {'msg': document.querySelector('#user_message').value,
        'username': username, 'room': room})

    }

    //join a room
    document.querySelectorAll('.select-room').forEach(p => {
        p.onclick = () => {
            let newroom = p.innerHTML
            
            // Check if user already in the room
            if (newroom === room) {
                msg = `You are already in ${room} room.`;
                prompt_message(msg);
            } else {
                exit_room(room);
                join_room(newroom);
                room = newroom;
            }
           
        }
    })

    //Leave room
    const exit_room = (room) => {
        socket.emit('leave', {'username': username, 'room': room})
        console.log(`${username} has left room ${room}`)
    }

    //Join room
    function join_room(room){
        socket.emit('join', {'username': username, 'room': room})
        console.log(`${username} has joined room ${room}`)

        //clear message area when user joins a chat room
        document.querySelector('#display-message-section').innerHTML = ''

        // Autofocus on text box
        document.querySelector("#user_message").focus();
    }

    //Print prompt message
    function prompt_message(msg){
        const p = document.createElement('p')
        p.innerHTML = msg
        document.querySelector('#display-message-section').append(p)
    }

})


