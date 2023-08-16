document.getElementById('order-by-select').addEventListener('change', function (event) {
    const url = new URL(window.location.href);
    const searchParams = new URLSearchParams(url.search);

    // Modify the query parameter
    searchParams.set('order_by', event.target.value);

    // Update the URL with modified query parameters
    url.search = searchParams.toString();

    // Replace the current URL with the modified URL
    window.history.replaceState(null, null, url);

    // Reload the page
    window.location.reload();
});

