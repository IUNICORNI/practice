const firstInput = document.getElementById('firstNumber');
const secondInput = document.getElementById('secondNumber');
const result = document.getElementById('result');
const buttons = document.querySelectorAll('button[data-action]');

function sum(a, b) {
  return a + b;
}

function difference(a, b) {
  return a - b;
}

function product(a, b) {
  return a * b;
}

function division(a, b) {
  if (b === 0) {
    throw new Error('Деление на ноль невозможно.');
  }
  return a / b;
}

function getValues() {
  const a = Number(firstInput.value.replace(',', '.'));
  const b = Number(secondInput.value.replace(',', '.'));

  if (!Number.isFinite(a) || !Number.isFinite(b)) {
    throw new Error('Ошибка: в оба поля нужно ввести числа.');
  }

  return { a, b };
}

function showResult(text, isError = false) {
  result.textContent = text;
  result.classList.toggle('error', isError);
}

buttons.forEach((button) => {
  button.addEventListener('click', () => {
    try {
      const { a, b } = getValues();
      let answer;

      switch (button.dataset.action) {
        case 'sum':
          answer = sum(a, b);
          break;
        case 'difference':
          answer = difference(a, b);
          break;
        case 'product':
          answer = product(a, b);
          break;
        case 'division':
          answer = division(a, b);
          break;
      }

      showResult(`Результат: ${answer}`);
    } catch (error) {
      showResult(error.message, true);
    }
  });
});
