const result = document.getElementById('result');
const plusBtn = document.getElementById('plusBtn');
const minusBtn = document.getElementById('minusBtn');
const message = document.getElementById('message');

let count = 0;

function updateView() {
  result.textContent = count;

  if (count > 0) {
    result.style.background = '#ffe66d';
  } else if (count < 0) {
    result.style.background = '#7bed9f';
  } else {
    result.style.background = '#ff6b6b';
  }

  plusBtn.disabled = count === 10;
  minusBtn.disabled = count === -10;

  if (count === 10 || count === -10) {
    message.textContent = 'Вы достигли экстремального значения';
  } else {
    message.textContent = '';
  }
}

plusBtn.addEventListener('click', () => {
  if (count < 10) {
    count += 1;
    updateView();
  }
});

minusBtn.addEventListener('click', () => {
  if (count > -10) {
    count -= 1;
    updateView();
  }
});

updateView();
