document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale: 'en', // Change this to your desired locale
        events: '/api/shifts', // Endpoint to fetch events
        eventRender: function(info) {
            // Customize event rendering
            info.el.querySelector('.fc-title').innerHTML =
                '<strong>Name:</strong> ' + info.event.extendedProps.name + '<br>' +
                '<strong>Shift Type:</strong> ' + info.event.extendedProps.shiftType;
        }
    });
    calendar.render();
});