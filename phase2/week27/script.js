let myCards = [
  {
    front: "Bonjour",
    back: "Hello",
  },
  {
    front: "Merci",
    back: "Thank you",
  },
  {
    front: "Pomme",
    back: "Apple",
  },
  {
    front: "Poisson",
    back: "Fish",
  },
  {
    front: "toujours",
    back: "always",
  },
];
let currentIndex = 0;
let isFront = true;



function flipCard(){
    let cardElement= document.getElementById("card");
    let textElement= document.getElementById("card-text")
    if(isFront){
        textElement.innerHTML=myCards[currentIndex].back;
        cardElement.classList.add("flipped");
        isFront=false
    }
    else{
        textElement.innerHTML=myCards[currentIndex].front;
        cardElement.classList.remove("flipped") 
        isFront=true
    }
}
function nextCard(){
    currentIndex++
    if(currentIndex>=myCards.length){
        currentIndex=0
    }
    isFront=true;
    let cardElement= document.getElementById("card");
    let textElement= document.getElementById("card-text")
    cardElement.classList.remove("flipped") 
    textElement.innerHTML=myCards[currentIndex].front
    let progress= document.getElementById("progress");
    progress.innerHTML = "cards " + (currentIndex + 1) + " of " + myCards.length;
}

window.onload = function () {
    document.getElementById("card-text").innerHTML = myCards[0].front;
  
    let progress = document.getElementById("progress");
    progress.innerHTML = "cards " + (currentIndex + 1) + " of " + myCards.length;
  };