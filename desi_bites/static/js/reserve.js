document.addEventListener('DOMContentLoaded', function() {
    const bookingForm = document.getElementById('booking-form');

    if (bookingForm) {
        bookingForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const formData = new FormData(bookingForm);
            const csrfToken = getCookie('csrftoken');

            fetch('http://localhost:8000/api/book/table', {
                method: 'POST',
                body: new URLSearchParams(formData).toString(),
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrfToken,
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Display a success toast
                    Swal.fire({
                        icon: 'success',
                        title: 'Table booked successfully',
                        showConfirmButton: false,
                        timer: 2000,
                    });
                    // Clear the form fields
                    bookingForm.reset();
                } else {
                    // Display an error toast
                    Swal.fire({
                        icon: 'error',
                        title: 'Failed to book the table',
                        showConfirmButton: false,
                        timer: 2000,
                    });
                }
            })
            .catch(error => {
                // Display an error toast for network or other errors
                Swal.fire({
                    icon: 'error',
                    title: 'An error occurred while processing your request',
                    showConfirmButton: false,
                    timer: 2000,
                });
            });
        });
    }
});

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
