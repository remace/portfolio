const CV_DOWN_FR = document.querySelector('#CV_fr')
const CV_DOWN_EN = document.querySelector('#CV_en')
const BUTTONS=[CV_DOWN_EN,CV_DOWN_FR]

BUTTONS.forEach(but =>{
    but.addEventListener('click',async function(){
        let lang='en'
        if (but === CV_DOWN_FR){
            lang='fr'
        }
        const response = await fetch(`./get-CV/${lang}`)
        const blob = await response.blob()
        console.log(`${lang}: ${blob.type}`)
        
        if (blob.type==='application/pdf'){
            //créer un lien invisible
            let link = document.createElement('a')
            link.style.display='none'
            //lui donner une URL locale de téléchargement et un nom pour le fichier téléchargé
            const url = URL.createObjectURL(blob)
            link.href=url
            link.download='CV_TAUVEL_Remi.pdf'
            document.body.appendChild(link)
            //lancer le téléchargement
            link.click()
            // supprimer le lien et l'URL locale de téléchargement
            window.URL.revokeObjectURL(url)
            document.body.removeChild(link)
        }
        else{
            window.location.href='/404/404'
        }
    })
})
