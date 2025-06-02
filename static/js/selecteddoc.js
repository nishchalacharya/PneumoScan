// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Function to handle doctor selection
function selectDoctor(selectedDoctor) {
    document.querySelectorAll('.doctor').forEach(doctor => {
        doctor.classList.remove('active');
    });
    selectedDoctor.classList.add('active');
    console.log(`Doctor selected: ${selectedDoctor.innerText.trim()}`);
}

// Function to handle date selection
function selectDate(selectedSlot) {
    document.querySelectorAll('.slot').forEach(slot => {
        slot.classList.remove('active');
    });
    selectedSlot.classList.add('active');
    console.log(`Date selected: ${selectedSlot.querySelector('span').innerText.trim()}`);
}

// Function to handle time selection
function selectTime(selectedTimeSlot) {
    document.querySelectorAll('.time-slot').forEach(slot => {
        slot.classList.remove('active');
    });
    selectedTimeSlot.classList.add('active');
    console.log(`Time selected: ${selectedTimeSlot.innerText.trim()}`);
}

// Function to send appointment data to the backend
function bookAppointment() {
    let selectedDoctor = document.querySelector('.doctor.active');
    let selectedSlot = document.querySelector('.slot.active');
    let selectedTimeSlot = document.querySelector('.time-slot.active');

    // Validate selection
    if (!selectedDoctor) {
        alert("Please select a doctor.");
        return;
    }
    if (!selectedSlot) {
        alert("Please select a valid date.");
        return;
    }
    if (!selectedTimeSlot) {
        alert("Please select a valid time.");
        return;
    }

    // Extract data
    let doctorName = selectedDoctor.innerText.trim();
    let selectedDate = selectedSlot.querySelector('span')?.innerText.trim();  // Extract only the date number
    let selectedTime = selectedTimeSlot.innerText.trim();

    console.log(`Booking appointment with: ${doctorName}, Date: ${selectedDate}, Time: ${selectedTime}`);

    // Send data to Django backend using Fetch API
    fetch('http://127.0.0.1:8000/loginapp/selectdoctor/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // CSRF token for security
        },
        body: JSON.stringify({
            doctor_name: doctorName,
            date: selectedDate,
            time: selectedTime
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(`Error: ${data.error}`);
        } else {
            alert("Appointment booked successfully!");
        }
    })
    .catch(error => console.error('Error:', error));
}
