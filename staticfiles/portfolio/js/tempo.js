const clock = document.querySelector(".clock");

window.addEventListener("load",time);

function time(){
  let date = new Date();
  let hrs = date.getHours();
  let min = date.getMinutes();
  let sec = date.getSeconds();
  min = check(min);
  sec = check(sec);
  clock.textContent = `${hrs}:${min}:${sec}`;
  setTimeout(time,1000);
}

function check(t){
  if(t < 10) return '0' + t;
  return t;
}