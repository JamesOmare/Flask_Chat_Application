document.addEventListener('DOMContentLoaded', () => {

    // enable submit message when 'enter' key is pressed
    let msg = document.querySelector('#user_message')
    msg.addEventListener('keyup', (e) => {
        e.preventDefault()
        if(e.key === 'Enter'){
            document.querySelector('#send_message').click()
        }
    })

    
})