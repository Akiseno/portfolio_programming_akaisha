function checkAnswers(){
    let score=0;
    let a1=document.getElementById("q1").value.toLowerCase().trim();
    console.log(a1)
    let a2=document.getElementById("q2").value.toLowerCase().trim();
    console.log(a2)
    let a3=document.getElementById("q3").value.toLowerCase().trim();
    console.log(a2)
    if (a1==="netherite"){
        score=score+1;
    }
    console.log(score);
    if (a2==="ominous potion"){
        score=score+1;
    }
    console.log(score);
    if (a3==="deep dark"){
        score=score+1;
    }
    console.log(score);
    let result=document.getElementById("result");
    result.innerHTML="you scored " + score + " points";

    if (score === 3) {
        result.style.color = "green";
    } else if (score === 0) {
        result.style.color = "red";
    } else {
        result.style.color = "orange";
    }
}