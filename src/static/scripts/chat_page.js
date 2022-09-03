document.addEventListener('DOMContentLoaded', () => {

     // Make sidebar collapse on click
     document.querySelector('#show-sidebar-button').onclick = () => {
        document.querySelector('#sidebar').classList.toggle('view-sidebar');
    };

    // enable submit message when 'enter' key is pressed
    let msg = document.querySelector('#user_message')
    msg.addEventListener('keyup', (e) => {
        e.preventDefault()
        if(e.key === 'Enter'){
            document.querySelector('#send_message').click()
        }
    })

    
})