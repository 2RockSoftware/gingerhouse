
// Shout out to https://codepen.io/Caediel for the snow affect! 


function createSnowflake() {
  const snowflake = document.createElement("i");
  snowflake.classList.add("fas", "fa-snowflake");
  snowflake.setAttribute(
    "style",
    `font-size: ${Math.random() * 10 +
      20}px; opacity: ${Math.random()}; left: ${Math.floor(
      Math.random() * window.innerWidth
    )}px; animation-duration: ${Math.random() * 5 + 3}s`
  );

  return snowflake;
}

setInterval(() => {
  if (
    [...document.querySelectorAll("i")][0] !== undefined &&
    [...document.querySelectorAll("i")][0].offsetTop === window.innerHeight
  )
    [...document.querySelectorAll("i")][0].remove();
  const snowflake = createSnowflake();
  document.body.appendChild(snowflake);
}, 200);