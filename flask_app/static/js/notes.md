1. ( 
    AJAX:
    validate using ajax
    show error messages without refreshing the page

    VALIDATIONS:
    all fields present both login and register
    first_name and last name MIN 2 characters
    email valid email address
    passwords must match
    ...use ajax to show error validations
)

basic syntax from: https://blog.logrocket.com/axios-vs-fetch-best-http-requests/#basic-syntax
### A better way to write fetch

```
// fetch()

const url = "https://jsonplaceholder.typicode.com/todos";
const options = {
  method: "POST",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json;charset=UTF-8",
  },
  body: JSON.stringify({
    a: 10,
    b: 20,
  }),
};
fetch(url, options)
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
  });
```

<br />

### A way to write axios 
```
// axios

const url = 'https://jsonplaceholder.typicode.com/posts'
const data = {
  a: 10,
  b: 20,
};
axios
  .post(url, data, {
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json;charset=UTF-8",
    },
  })
  .then(({data}) => {
    console.log(data);
});
```