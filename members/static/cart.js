let boxes = document.querySelectorAll('.box')
let amounts = document.querySelectorAll('.amount')
let prices = document.querySelectorAll('.price')
let username = document.querySelector('.username')
let form = document.querySelector('form')

let deltaAmount = document.querySelectorAll('.up-down')

let i = 0;
for (key in deltaAmount)
{
    try
    {   
        el = deltaAmount[key].children
        el[1].parentElement.id = i

        el[0].addEventListener('click',(e)=>{
            let uname = e.target.parentElement.parentElement.children[0].innerText
            let fname = e.target.parentElement.parentElement.children[1].innerText
            let price = e.target.parentElement.parentElement.children[2]
            let amount = e.target.parentElement.parentElement.children[3]

            i_p = parseInt(price.innerText)
            i_a = parseInt(amount.innerText)
            i_p_b = i_p/i_a

            price.innerText = Math.abs(i_p_b*(++i_a))
            amount.innerText = Math.abs(i_a)

            csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;
            fetch(`/Cart/${fname}/${1}/${i_p_b}`,{method:'POST',headers: {'X-CSRFToken': csrfToken,'Content-Type': 'application/json'}})

            const itemnameElements = document.querySelectorAll('.itemname');

            // Initialize an array to store the innerText values
            const innerTextArray = [];

            // Iterate through the elements and extract their innerText
            itemnameElements.forEach(element => {
            innerTextArray.push(element.innerText);
            });

            // Create a JSON object with the innerText values
            const jsonResult = JSON.stringify({ iname: innerTextArray });   
            const encodedJsonResult = encodeURIComponent(jsonResult);
            form.action = `/Order/${price.innerText}/${jsonResult}`
            console.log(form.action);
        })
        el[1].addEventListener('click',(e)=>{
            let uname = e.target.parentElement.parentElement.children[0].innerText
            let fname = e.target.parentElement.parentElement.children[1].innerText
            let price = e.target.parentElement.parentElement.children[2]
            let amount = e.target.parentElement.parentElement.children[3]

            let i_p = parseInt(price.innerText)
            let i_a = parseInt(amount.innerText)
            let i_p_b = i_p/i_a

            price.innerText = Math.abs(i_p_b*(--i_a))
            amount.innerText = Math.abs(i_a)

            console.log(`/Cart/${fname}/${-1}/${-i_p_b}`);

            csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;
            fetch(`/Cart/${fname}/${-1}/${-i_p_b}`,{method:'POST',headers: {'X-CSRFToken': csrfToken,'Content-Type': 'application/json'}})
        })
    }
    catch
    {

    }
    i++
}