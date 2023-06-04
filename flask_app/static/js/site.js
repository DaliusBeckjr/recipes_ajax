

async function validate_login(e) {
    // e - is another way to say 'event'

    e.preventDefault();
    // console.log('you made it to login')
    formData = new FormData(login);

    let response = await fetch('http://localhost:5000/users/login_validation', {method : 'POST', body : formData})

    let data = await response.json()
    console.log(data)


    if ('error' in data) {
        login_error.innerHTML = `
            <p class="text-danger"> Invalid Credentials </p>
        `
    }

}

async function validate_reg(e) {

    e.preventDefault();

    formData = new FormData(reg_form);

    let response = await fetch('http://localhost:5000/users/reg_validation', {method : 'POST', body : formData} )

    let data = await response.json()
    console.log(data)

    if ('error' in data) {
        reg_error.innerHTML = " "
        if ('first_name' in data.error) {
            reg_error.innerHTML += ` 
                <p class="text-danger"> ${data.error.first_name} </p>
            `
        }
        if ('last_name' in data.error) {
            reg_error.innerHTML += ` 
                <p class="text-danger"> ${data.error.last_name} </p>
            `
        }
        if ('email' in data.error) {
            reg_error.innerHTML += ` 
                <p class="text-danger"> ${data.error.email} </p>
            `
        }
        if ('email_format' in data.error) {
            reg_error.innerHTML += ` 
                <p class="text-danger"> ${data.error.email_format} </p>
            `
        }
        if ('password' in data.error) {
            reg_error.innerHTML += ` 
                <p class="text-danger"> ${data.error.password} </p>
            `
        }
        if ('confirm_pw' in data.error) {
            reg_error.innerHTML += ` 
                <p class="text-danger"> ${data.error.confirm_pw} </p>
            `
        }
    } else {
        register()
    }
}


async function register() {
    formData = new FormData(reg_form)
    let response = await fetch('http://localhost:5000/users/registration', {method : 'POST', body : formData} )

    let data = await response.json()
    console.log(data)

    if(data.status == 201) {
        window.location.href = "http://localhost:5000/recipes/dashboard"
    }
}

async function getRecipes() {
    let response = await fetch('http://localhost:5000/recipes')
    let data = await response.json()
    console.log(data)
}

async function validate_recipe(e) {
    e.preventDefault();

    formData = new FormData(recipe_form);

    let response = await fetch('http://localhost:5000/recipes/recipe_validation', {method : 'POST', body : formData} )
    let data = response.json()
    console.log(data)
    
}