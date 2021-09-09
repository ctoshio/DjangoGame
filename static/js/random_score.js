var score = 0;

function randomScore() {
  score = Math.floor(Math.random() * 1000001);
  document.getElementById('playerscards').value = score;
  document.getElementById('btn1').disabled = true;
}