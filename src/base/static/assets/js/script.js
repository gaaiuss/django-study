function myScope() {
    const form = document.querySelector('.form-grid');
    const button = document.querySelector('button');
    const people = [];

    function receiveEventForm (event) {
        const firstName = form.querySelector('#first-name');
        const lastName = form.querySelector('#last-name');
        const email = form.querySelector('#email');
        const message = form.querySelector('#message');

        people.push({
            firstName: firstName.value,
            lastName: lastName.value,
            email: email.value,
            message: message.value
        });

        console.log(people);
    }

    button.addEventListener('click', receiveEventForm);
}

myScope();