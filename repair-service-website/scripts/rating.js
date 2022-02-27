function starFixed() {
    for (i=1;i<=5;i++) {
        star = document.querySelector(`#star-${i}`)
        star.removeAttribute("onmouseover");
        star.removeAttribute("onclick");
        star.setAttribute("onclick", `starFill${i}()`);
    }
    document.querySelector("#rating").removeAttribute("onmouseout");        
}

function starFill0() {
    [...document.querySelectorAll(".rating-star")].forEach(star => {
        star.classList = "bi bi-star-fill text-secondary rating-star px-1";
    })
}

function starFill1() {
    document.querySelector("#star-1").classList = "bi bi-star-fill text-info rating-star px-1";
    document.querySelector("#star-2").classList = "bi bi-star-fill text-secondary rating-star px-1";
    document.querySelector("#star-3").classList = "bi bi-star-fill text-secondary rating-star px-1";
    document.querySelector("#star-4").classList = "bi bi-star-fill text-secondary rating-star px-1";
    document.querySelector("#star-5").classList = "bi bi-star-fill text-secondary rating-star px-1";
}

function starFill2() {
    document.querySelector("#star-1").classList = "bi bi-star-fill text-info rating-star px-1";
    document.querySelector("#star-2").classList = "bi bi-star-fill text-info rating-star px-1";
    document.querySelector("#star-3").classList = "bi bi-star-fill text-secondary rating-star px-1";
    document.querySelector("#star-4").classList = "bi bi-star-fill text-secondary rating-star px-1";
    document.querySelector("#star-5").classList = "bi bi-star-fill text-secondary rating-star px-1";
}

function starFill3() {
    document.querySelector("#star-1").classList = "bi bi-star-fill text-info rating-star px-1";
    document.querySelector("#star-2").classList = "bi bi-star-fill text-info rating-star px-1";
    document.querySelector("#star-3").classList = "bi bi-star-fill text-info rating-star px-1";
    document.querySelector("#star-4").classList = "bi bi-star-fill text-secondary rating-star px-1";
    document.querySelector("#star-5").classList = "bi bi-star-fill text-secondary rating-star px-1";
}

function starFill4() {
    document.querySelector("#star-1").classList = "bi bi-star-fill text-info rating-star px-1";
    document.querySelector("#star-2").classList = "bi bi-star-fill text-info rating-star px-1";
    document.querySelector("#star-3").classList = "bi bi-star-fill text-info rating-star px-1";
    document.querySelector("#star-4").classList = "bi bi-star-fill text-info rating-star px-1";
    document.querySelector("#star-5").classList = "bi bi-star-fill text-secondary rating-star px-1";
}

function starFill5() {
    document.querySelector("#star-1").classList = "bi bi-star-fill text-info rating-star px-1";
    document.querySelector("#star-2").classList = "bi bi-star-fill text-info rating-star px-1";
    document.querySelector("#star-3").classList = "bi bi-star-fill text-info rating-star px-1";
    document.querySelector("#star-4").classList = "bi bi-star-fill text-info rating-star px-1";
    document.querySelector("#star-5").classList = "bi bi-star-fill text-info rating-star px-1";
}