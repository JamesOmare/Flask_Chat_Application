document.addEventListener('DOMContentLoaded', () => {

    //reload window to fix render bug
    reload()
    
    
    //connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port)

    //get username
    const username = document.querySelector('#get-username').innerHTML
    
    //default room 
    let room = 'Music'
    join_room('Music')

    // displays message in terminal when connection to server is made
    socket.on('connect', () => {
        console.log('connected to server')
        
    })

    // send message
    document.querySelector('#send_message').onclick = () =>{
        socket.emit('message', {'msg': document.querySelector('#user_message').value,
        'username': username, 'room': room})
    
    //clear input area when sending message
    document.querySelector('#user_message').value = ''

    }

    //Display incoming messages
    socket.on('message', data => {

        //display message when received
        if(data.msg){
            const p = document.createElement('p')
            const user = document.createElement('span')
            const time_stamp = document.createElement('span')
            const br = document.createElement('br')
            const message = document.createElement('span')

            
            //display user's message
            if(data.username === username){
                p.setAttribute("class", "my-msg")

                //username
                user.setAttribute("class", "my-username")
                user.innerHTML = data.username

                //message
                message.setAttribute('class', 'message_data')
                message.innerHTML = data.msg

                //timestamp
                time_stamp.setAttribute("class", "timestamp")
                time_stamp.innerHTML = data.timestamp


                //HTML to append
                p.innerHTML = user.outerHTML+ br.outerHTML + message.outerHTML + br.outerHTML + time_stamp.outerHTML

                //append
                document.querySelector('#display-message-section').append(p)

            }
            
            //Display other users' messages
            else if(typeof data.username !== 'undefined'){
                p.setAttribute("class", "others-msg")

                //username
                user.setAttribute("class", "other-username")
                user.innerHTML = data.username

                //message
                message.setAttribute('class', 'message_data')
                message.innerHTML = data.msg

                //timestamp
                time_stamp.setAttribute("class", "other_timestamp")
                time_stamp.innerHTML = data.timestamp

                //HTML to append
                p.innerHTML = user.outerHTML+ br.outerHTML + message.outerHTML + br.outerHTML + time_stamp.outerHTML

                //append
                document.querySelector('#display-message-section').append(p)
            }

            //Display system message
            else{
                prompt_message(data.msg)
            }
        }
       
        scroll_down_chat()
        
    })


    socket.on('disconnect', () => {
        // console.log('disconnected from server')
        socket.emit('client has been disconnected')
    })

    

    //join a room
    document.querySelectorAll('.select-room').forEach(p => {
        p.onclick = () => {
        
           let newroom = p.innerText  
            
            // Check if user already in the room
            if (newroom == room) {
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
        
    }

    //Join room
    function join_room(room){
        socket.emit('join', {'username': username, 'room': room})
       

        //clear message area when user joins a chat room
        document.querySelector('#display-message-section').innerHTML = ''

        // Autofocus on text box
        document.querySelector("#user_message").focus();
    }


    // Scroll down chat window when message section fills screen
    function scroll_down_chat() {
        const chatWindow = document.querySelector("#display-message-section");
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }


    //Print prompt message
    function prompt_message(msg){
        const p = document.createElement('p')
        p.setAttribute('class', 'system-msg')
        p.innerHTML = msg

        const alert_prompt = document.createElement('p')
        alert_prompt.setAttribute('class', 'alert-msg')
        
        //remove all html tags to get message string 
        let x = p.innerHTML
        let div = document.createElement("div");
        div.innerHTML = x
        let text = div.textContent || div.innerText || ""
        alert_prompt.innerHTML = text
      

        document.querySelector('#display-message-section').append(alert_prompt)
        scroll_down_chat()

        //focus on text box
        document.querySelector('#user_message').focus()
    }

    // function to reload page once
    function reload()
    {
        if( window.localStorage )
        {
            console.log('page reloaded')
            if( !localStorage.getItem('firstLoad') )
            {
            localStorage['firstLoad'] = true;
            window.location.reload();
            }  
            else
            localStorage.removeItem('firstLoad');
        }
    }
        
        

})
