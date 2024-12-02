document.addEventListener('DOMContentLoaded', () => {
    // Поля формы и их настройки
    const fields = [
        { selector: '.series1', regex: /^[0-9]{0,4}$/, errorSelector: '.series1-error', errorMessage: 'Поле должно содержать 4 цифры 0-9' },
        { selector: '.number', regex: /^[ABCEHIKMOPTX]{0,2}$/, errorSelector: '.number-error', errorMessage: 'Поле должно содержать 2 латинские буквы A,B,C,E,H,I,K,M,O,P,T,X' },
        { selector: '.series2', regex: /^[0-7]{0,1}$/, errorSelector: '.series2-error', errorMessage: 'Поле должно содержать одну цифру 0-7' },
    ];

    fields.forEach((field, index) => {
        const currentField = document.querySelector(field.selector);
        if (currentField) {
            currentField.addEventListener('input', () => {
                // Преобразование в верхний регистр для поля "number"
                if (field.selector === '.number') {
                    currentField.value = currentField.value.toUpperCase();
                }
                validateInput(currentField, field.regex, field.errorSelector, field.errorMessage);
            });

            autoTab(
                currentField,
                currentField.maxLength,
                fields[index + 1] ? fields[index + 1].selector : null,
                fields[index - 1] ? fields[index - 1].selector : null
            );
        }
    });
});

// Функция для валидации во время ввода
function validateInput(field, regex, errorSelector, errorMessage) {
    const errorElement = document.querySelector(errorSelector);
    if (!regex.test(field.value)) {
        field.value = field.value.slice(0, -1); // Удаляем последний некорректный символ
        errorElement.textContent = errorMessage;
        errorElement.style.display = 'block';
    } else {
        errorElement.style.display = 'none';
    }
}

// Переход между полями
function autoTab(current, maxLength, nextSelector, prevSelector) {
    const nextField = nextSelector ? document.querySelector(nextSelector) : null;
    const prevField = prevSelector ? document.querySelector(prevSelector) : null;

    current.addEventListener('input', () => {
        // Если поле заполнено, переходим на следующее
        if (current.value.length === maxLength && nextField) {
            nextField.focus();
        }
    });

    current.addEventListener('keydown', (e) => {
        // Переход на предыдущее поле при нажатии Backspace
        if (e.key === "Backspace" && current.value.length === 0 && prevField) {
            prevField.focus();
        }
    });
}
