let frenchDivs = document.querySelectorAll('.fr')
let englishDivs = document.querySelectorAll('.en')
const SWITCH_LANGUAGE_BUTTON = document.querySelector('#languageSwitcher')

SWITCH_LANGUAGE_BUTTON.addEventListener('click', function(){
    frenchDivs.forEach(div => {
        div.classList.toggle('hidden')
    });
    englishDivs.forEach(div => {
        div.classList.toggle('hidden')
    })
    if (SWITCH_LANGUAGE_BUTTON.innerHTML == "Switch to English"){
        SWITCH_LANGUAGE_BUTTON.innerHTML = "Lire en Français"
        console.log("page traduite en anglais")
        
    }else if (SWITCH_LANGUAGE_BUTTON.innerHTML == "Lire en Français"){
        SWITCH_LANGUAGE_BUTTON.innerHTML = "Switch to English"
        console.log("page traduite en français")
    }else{
        console.log("erreur, le texte un problème")
        console.log(SWITCH_LANGUAGE_BUTTON.innerHTML)
    }
})
