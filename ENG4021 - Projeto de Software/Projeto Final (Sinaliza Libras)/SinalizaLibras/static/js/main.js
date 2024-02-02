function check(){

  var question1 = document.quiz.question1.value;
  var question2 = document.quiz.question2.value;
  var question3 = document.quiz.question3.value;
  var question4 = document.quiz.question4.value;
  var question5 = document.quiz.question5.value;
  var question6 = document.quiz.question6.value;
  var question7 = document.quiz.question7.value;
  var question8 = document.quiz.question8.value;
  var question9 = document.quiz.question9.value;
  var question10 = document.quiz.question10.value;
  var question11 = document.quiz.question11.value;

  var correct = 0;

  if (question1 == "CARLA, MARIA, CAIO, ANA"){
      correct++;
  }
  if (question2 == "C") {
      correct++;
  }

  if (question3 == "L") {
      correct++;
  }

  if (question4 == "Y") {
      correct++;
  }

  if (question5 == "G") {
      correct++;
  }

  if (question6 == "A") {
      correct++;
  }
  
  if (question7 == "B") {
      correct++;
  }

  if (question8 == "D") {
      correct++;
  }

  if (question9 == "F") {
      correct++;
  }

  if (question10 == "SÔNIA, SOFIA, OSIAS, OSNI") {
      correct++;
  }

  if (question11 == "ANA, MARIA, MARIANA, MARTA, RITA") {
      correct++;
  }

  document.getElementById("after_submit").style.visibility="visible";

  document.getElementById("number_correct").innerHTML = "Acertou " + correct + " questoes.";

}

// reflesh page function

function myFunction() {
    location.reload();
}
