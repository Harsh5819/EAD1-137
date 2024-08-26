document.addEventListener('DOMContentLoaded', () => {
    const display = document.getElementById('display');
    const buttons = document.querySelectorAll('.btn');
    let currentInput = '';
    let operator = '';
    let firstOperand = '';

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const value = button.getAttribute('data-value');

            if (value === 'C') {
                display.textContent = '';
                currentInput = '';
                operator = '';
                firstOperand = '';
            } else if (value === '=') {
                if (firstOperand && operator && currentInput) {
                    display.textContent = eval(`${firstOperand}${operator}${currentInput}`);
                    currentInput = display.textContent;
                    operator = '';
                    firstOperand = '';
                }
            } else if (['+', '-', '*', '/'].includes(value)) {
                firstOperand = currentInput;
                operator = value;
                currentInput = '';
            } else {
                currentInput += value;
                display.textContent = currentInput;
            }
        });
    });
});
