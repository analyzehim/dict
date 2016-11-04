ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map("map", {
            center: [55.745508, 37.435225],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        });

    // Добавим на карту схему проезда
    // от улицы Крылатские холмы до станции метро "Кунцевская"
    // через станцию "Молодежная" и затем до станции "Пионерская".
    // Точки маршрута можно задавать 3 способами:
    // как строка, как объект или как массив геокоординат.
    ymaps.route([
        [55.843535, 37.495861],//Россия, Москва, Кронштадтский бульвар  19 корпус 2
        [55.698923, 37.531505], //ВМК
    ]).then(function (route) {


        var moveList = ('Пробки '+route.getJamsTime()+'<br>'),
            way,
            segments;
        moveList+=('Без пробок '+route.getTime()+'<br>');
        moveList+=('Длина '+route.getLength()+'<br>');
        // Выводим маршрутный лист.
        $('#list').append(moveList);
    }, function (error) {
        alert('Возникла ошибка: ' + error.message);
    });
}