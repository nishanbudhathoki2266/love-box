const sendLove = document.querySelector('.btn--open-form');
const goBack = document.querySelector('.btn--back');
const btnCloseFlash = document.querySelector('.flash-messages__btn');
const loveBoxContainer = document.querySelector('.love-box');
const formContainer = document.querySelector('.form-container');
const messageForm = document.querySelector('#form');
const messageBox = document.querySelector('#messageBox');
const flashMessagesContainer = document.querySelector('.flashes');

const toggleContent = () => {
    loveBoxContainer.classList.toggle('hidden');
    formContainer.classList.toggle('hidden');
}

[sendLove, goBack].forEach(btn => {
    btn.addEventListener('click', function (e) {
        e.preventDefault();
        toggleContent();
    });
})

setTimeout(() => {
    flashMessagesContainer.style.display = 'none';
}, 5000);

btnCloseFlash.addEventListener('click', function (e) {
    e.preventDefault();
    flashMessagesContainer.style.display = 'none';
});


