/* Abre e fecha menu lateral em modo mobile */

const menuMobile = document.querySelector('.menu-mobile');
const body = document.querySelector('body');

menuMobile.addEventListener('click', () =>{
    menuMobile.classList.contains("bi-list")
    ? menuMobile.classList.replace('bi-list', 'bi-x')
    : menuMobile.classList.replace("bi-x", 'bi-list');
    body.classList.toggle("menu-nav-active")
})

//Troca a aba ativa para a que foi clicada

function ativarLink(linkClicado){
    const linkAtivo = document.querySelectorAll('.nav-link.active');

    linkAtivo.forEach(function(link) {
        link.classList.remove('active');
    })
    linkClicado.classList.add('active');
}

document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');

    // Create an observer to watch each section
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Remove 'active' from all links
                navLinks.forEach(link => link.classList.remove('active'));
                // Add 'active' to the link corresponding to the intersecting section
                const currentId = entry.target.id;
                document.querySelector(`.nav-link[href="#${currentId}"]`).classList.add('active');
            }
        });
    }, {
        // Options: rootMargin makes it trigger a bit before the section hits the top
        rootMargin: '0%', // Adjust as needed (e.g., '-50% 0px -50% 0px')
        threshold: 0.5 // Trigger when 10% of the section is visible
    });

    // Observe each section
    sections.forEach(section => {
        observer.observe(section);
    });
});

/* Fecha o menu quando clicar em algum item e muda o icone para list */

const navItem = document.querySelectorAll('.nav-item')

navItem.forEach(item => {
    item.addEventListener("click", () => {
        if (body.classList.contains("menu-nav-active")) {
            body.classList.remove("menu-nav-active")
            menuMobile.classList.replace("bi-x", "bi-list")
        }
    })
})

// Animação de quem tiver o atributo data-anime

const item = document.querySelectorAll("[data-anime]");

const animeScroll = () => {
    const windowTop = window.pageYOffset + window.innerHeight * 0.85;

    item.forEach(element=>{
        if (windowTop > element.offsetTop){
            element.classList.add('animate')
        }
        else{
            element.classList.remove('animate')
        }
    })
}

animeScroll()

window.addEventListener("scroll", ()=>{
    animeScroll();
})