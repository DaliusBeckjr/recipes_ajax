const { default: axios } = require("axios");

async function validate_login(e) {
    e.preventDefault();


    formData = new FormData(login);

    backendURI = 'http://localhost:5000/users/login_validation';
    data = formData

    res = await axios.post(backendURI, data, {
        headers: {'Content-Type': 'appllication/json'},
    })
    .then(res => console.log(res.data))
    .catch(err => console.error(err))

    if ('error' in data) {

    } 
}
