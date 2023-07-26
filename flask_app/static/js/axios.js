const { default: axios } = require("axios");

function validate_login(e) {
    e.preventDefault();


    formData = new FormData(login);

    axios({
        method: 'post',
        url: 'http://localhost:5000/users/login_validation',
        data: FormData,
        headers: {'Content-Type': 'multipart/form-data'},
    })
    .then(res => console.log(res.data))
    .catch(err => console.error(err))

    if ('error' in data) {

    } 
}
