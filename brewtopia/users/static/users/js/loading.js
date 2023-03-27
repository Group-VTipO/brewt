window.addEventListener("load", function () {
    const loader = document.querySelector(".loader");
    loader.className += " hidden"; // скрываем loader
    setTimeout(function(){ window.location.href = "{% url 'users:home' %}"; }, 2000); // переход на главную через 2 секунды
});
