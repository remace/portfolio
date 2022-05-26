const ESCAPE_BUTTONS = document.getElementsByName("escape_message")

ESCAPE_BUTTONS.forEach(button => {
    button.addEventListener('click', function(){
        let messageBox = this.parentElement
        messageBox.parentElement.removeChild(messageBox)
    })
})