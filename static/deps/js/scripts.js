/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.querySelector('input[type="file"]');
    const previewContainer = document.getElementById('preview-container');

    fileInput.addEventListener('change', function(event) {
        const files = event.target.files;
        previewContainer.innerHTML = ''; // Очистить контейнер перед новым выбором

        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            if (file) {
                const reader = new FileReader();
                
                reader.onload = function(e) {
                    const img = document.createElement('img');
                    img.src = e.target.result;
                    img.style.maxWidth = '200px'; // Ограничьте размер превью
                    img.style.margin = '10px'; // Добавьте отступ
                    previewContainer.appendChild(img); // Добавляем изображение в контейнер
                }

                reader.readAsDataURL(file); // Читаем файл как DataURL
            }
        }
    });
});
