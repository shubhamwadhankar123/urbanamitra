function bookService(serviceName, image, description, price) {
    // Save selected service details in session storage
    sessionStorage.setItem("serviceName", serviceName);
    sessionStorage.setItem("image", image);
    sessionStorage.setItem("description", description);
    sessionStorage.setItem("price", price);

    // Check if user is logged in (check session storage or cookies)
    let loggedIn = sessionStorage.getItem("loggedIn");

    if (!loggedIn) {
        // Redirect to login page if not logged in
        window.location.href = "login.html";
    } else {
        // If logged in, proceed to location page
        window.location.href = "location.html";
    }
}
