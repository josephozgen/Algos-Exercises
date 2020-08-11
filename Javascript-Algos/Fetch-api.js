fetch('url')
    .then(
        response => {
            console.log(response);
        },
        rejection => {
            console.error(rejection.message);
        }
    );

fetch1(url, {
    method: 'POST',
    headers: {
        'Content-type': 'application/json',
        'apikey': apiKey
    },
    body: data
})
.then(
    response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Request failed!');
    },
    networkError => {
        console.log(networkError.message)
    }
    );

