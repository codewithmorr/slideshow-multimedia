let currentSlide = 0;
let slides = document.querySelectorAll('.slide');
let sound = document.getElementById('clickSound');
let progressBar = document.getElementById('progressBar');

function updateProgressBar() {
    let progress = ((currentSlide + 1) / slides.length) * 100;
    progressBar.style.width = progress + '%';
}

function showSlide(index) {
    slides.forEach(slide => slide.classList.remove('active'));
    slides[index].classList.add('active');
    currentSlide = index;
    updateProgressBar();
}

function nextSlide(){
    if(currentSlide < slides.length - 1){
        currentSlide++;
        showSlide(currentSlide);
        if(sound) sound.play();
    }
}

function prevSlide(){
    if(currentSlide > 0){
        currentSlide--;
        showSlide(currentSlide);
        if(sound) sound.play();
    }
}

// initialize
updateProgressBar();

let bgmusic = document.getElementById('bgmusic');
let musicStarted = false;

function startMusic() {
    if (!musicStarted) {
        bgmusic.volume = 0.1;
        bgmusic.play();
        musicStarted = true;
    }
}

function showSLide(index) {
    startMusic();

    slides.forEach(slide => slide.classList.remove('active'));

    slides[index].classList.add('active');
    currentSlide = index;
    updateProgressBar();
    if(sound) sound.play();
}

