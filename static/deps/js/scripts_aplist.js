document.addEventListener("DOMContentLoaded", function () {
    const imageContainer = document.getElementById("imageContainer");
    const gosNumberInput = document.getElementById("gosNumberInput");

    // Инициализация перетаскивания
    new Sortable(imageContainer, {
        animation: 150,
        onEnd: function () {
            updateOrder();
        }
    });

    // Функция для обновления порядка изображений
    function updateOrder() {
        const images = imageContainer.querySelectorAll(".image-item");
        const orderData = Array.from(images).map((item, index) => ({
            id: item.dataset.id,
            order: index + 1
        }));
        document.getElementById("orderInput").value = JSON.stringify(orderData);
    }

    // Обработчик для удаления изображения
    imageContainer.addEventListener("click", function (event) {
        if (event.target.classList.contains("delete-button")) {
            const imageItem = event.target.closest(".image-item");
            imageItem.remove();
            updateOrder();
        }
    });

    // Сохранение изменений
    document.getElementById("saveButton").addEventListener("click", function () {
        const formData = new FormData();
        formData.append("gos_number", gosNumberInput.value);
        formData.append("order", document.getElementById("orderInput").value);

        fetch("/save-moderation-changes/", {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": getCsrfToken()
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Изменения успешно сохранены!");
            } else {
                alert("Ошибка сохранения изменений.");
            }
        });
    });

    function getCsrfToken() {
        return document.querySelector("[name=csrfmiddlewaretoken]").value;
    }
});