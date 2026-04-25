let currentSlide = 0;
let slides = document.querySelectorAll(".slide");
let progressBar = document.getElementById("progressBar");
let sound = document.getElementById("clickSound");

let currentLink = "";

// update progress
function updateProgress(){
    let progress = ((currentSlide + 1) / slides.length) * 100;
    progressBar.style.width = progress + "%";
}

// show slide
function showSlide(index){
    slides.forEach(slide => slide.classList.remove("active"));
    slides[index].classList.add("active");
    currentSlide = index;
    updateProgress();
    if(sound) sound.play();
}

// next
function nextSlide(){
    if(currentSlide < slides.length - 1){
        showSlide(currentSlide + 1);
    }
}

// open album internally
function openAlbum(title, image, artist, link){
    document.getElementById("detailTitle").innerText = title;
    document.getElementById("detailImage").src = image;
    document.getElementById("detailArtist").innerText = artist;
    currentLink = link;

    showSlide(2); // detail slide
}

// open spotify
function openSpotify(){
    window.open(currentLink, "_blank");
}

// init
updateProgress();