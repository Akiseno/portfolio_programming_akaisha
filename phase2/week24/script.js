function checkAnswers() {
  let score = 0;
  let a1 = document.getElementById("q1").value.toLowerCase().trim();
  console.log(a1);
  let a2 = document.getElementById("q2").value.toLowerCase().trim();
  console.log(a2);
  let a3 = document.getElementById("q3").value.toLowerCase().trim();
  console.log(a3);
  let a4 = document.getElementById("q4").value.toLowerCase().trim();
  console.log(a4);
  let a5 = document.getElementById("q5").value.toLowerCase().trim();
  console.log(a5);

  let feedback1 = document.getElementById("feedback1");
  let feedback2 = document.getElementById("feedback2");
  let feedback3 = document.getElementById("feedback3");
  let feedback4 = document.getElementById("feedback4");
  let feedback5 = document.getElementById("feedback5");

  if (a1 === "netherite") {
    feedback1.innerHTML = "correct";
    feedback1.classList.remove("incorrect");
    feedback1.classList.add("correct");
    score = score + 1;
  } else {
    feedback1.innerHTML = "incorrect";
    feedback1.classList.remove("correct");
    feedback1.classList.add("incorrect");
  }
  console.log(score);

  if (a2 === "ominous bottle") {
    feedback2.innerHTML = "correct";
    feedback2.classList.remove("incorrect");
    feedback2.classList.add("correct");
    score = score + 1;
  } else {
    feedback2.innerHTML = "incorrect";
    feedback2.classList.remove("correct");
    feedback2.classList.add("incorrect");
  }
  console.log(score);

  if (a3 === "deep dark") {
    feedback3.innerHTML = "correct";
    feedback3.classList.remove("incorrect");
    feedback3.classList.add("correct");
    score = score + 1;
  } else {
    feedback3.innerHTML = "incorrect";
    feedback3.classList.remove("correct");
    feedback3.classList.add("incorrect");
  }
  console.log(score);

  if (a4 === "sparsed jungle") {
    feedback4.innerHTML = "correct";
    feedback4.classList.remove("incorrect");
    feedback4.classList.add("correct");
    score = score + 1;
  } else {
    feedback4.innerHTML = "incorrect";
    feedback4.classList.remove("correct");
    feedback4.classList.add("incorrect");
  }
  console.log(score);

  if (a5 === "wooded badlands") {
    feedback5.innerHTML = "correct";
    feedback5.classList.remove("incorrect");
    feedback5.classList.add("correct");
    score = score + 1;
  } else {
    feedback5.innerHTML = "incorrect";
    feedback5.classList.remove("correct");
    feedback5.classList.add("incorrect");
  }
  console.log(score);

  let result = document.getElementById("result");
  result.innerHTML = "you scored " + score + " points";

  if (score === 5) {
    result.style.color = "green";
  } else if (score === 0) {
    result.style.color = "red";
  } else {
    result.style.color = "orange";
  }
}

function resetGame() {

  document.getElementById("q1").value = "";
  document.getElementById("q2").value = "";
  document.getElementById("q3").value = "";
  document.getElementById("q4").value = "";
  document.getElementById("q5").value = "";

  let feedbacks = ["feedback1", "feedback2", "feedback3", "feedback4", "feedback5"];
  feedbacks.forEach(function (id) {
    let el = document.getElementById(id);
    el.innerHTML = "";
    el.classList.remove("correct", "incorrect");
  });

  document.getElementById("result").innerHTML = "";
}
