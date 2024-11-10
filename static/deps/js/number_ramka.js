// Функция для валидации во время ввода
function validateInput(field, regex, errorSelector, errorMessage) {
    if (!regex.test(field.value)) {
        field.value = field.value.slice(0, -1);  // Удаляем последний введённый символ, если он некорректен
        document.querySelector(errorSelector).textContent = errorMessage;
        document.querySelector(errorSelector).style.display = 'block';
    } else {
        document.querySelector(errorSelector).style.display = 'none';
    }
}

// Переход между полями при заполнении
function autoTab(current, maxLength, nextSelector, prevSelector) {
    if (current.value.length === maxLength && nextSelector) {
        const nextField = document.querySelector(nextSelector);
        if (nextField) {
            nextField.focus();
        }
    } else if (current.value.length === 0 && prevSelector) {
        const prevField = document.querySelector(prevSelector);
        if (prevField) {
            prevField.focus();
        }
    }
}