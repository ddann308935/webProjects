// attach interactivity to HTML
// javascript responds to events
// to connect js to HTML, use id

function onLoad() {
    // create variables for button and navigation
    const navbutton = document.querySelector("#nav-button")
    const mainnav = document.querySelector("#main-nav")

    // click button with conditionals, NULL function
    navbutton.addEventListener('click', function(){
        if (mainnav.classList.contains('open')) {
            // if open, then close
            mainnav.classList.remove('open')
        }
        else {
            // if close, then open
            mainnav.classList.add('open')
        }
    })
}

// waiting for document to load
// 'load' is a HTML event, onLoad is a js function
window.addEventListener('load', onLoad )
