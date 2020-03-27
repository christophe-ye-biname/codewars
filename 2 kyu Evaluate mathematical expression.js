const Calculator = function() {
  this.evaluate = string => {
    function calc(str)
{
    
    str = str.split(" ");
    while (str.length > 1)
    {
        for (let i = 0; i < str.length; i++)
        {
            if (str[i] == "/")
            {
                str = divi(str, i);
                i = 0;
            }
            else if (str[i] == "*")
            {
                str = mult(str ,i);
                i = 0;
            }
            
        }
        for (let i = 0; i < str.length; i++)
        {
            if (str[i] == "+")
            {
                str = add(str, i);
                i = 0;
            }
            else if (str[i] == "-")
            {
                str = sous(str, i);
                i = 0;
            }
           
        }
        
    }
    return str;
}
function mult(arr, i)
{
    let mult = [];
    let inter = parseFloat(arr[i-1]) * parseFloat(arr[i+1]);
    for (let j = 0; j < arr.length; j++)
    {
        if (j < i-1)
        {
            mult.push(arr[j]);
        }
        else if (j == i)
        {
            mult.push(inter);
        }
        else if (j > i+1)
        {
            mult.push(arr[j]);
        }
    }
    return mult
}
return calc(string);
function divi(arr, i)
{
    let div = [];
    let inter = parseFloat(arr[i-1]) / parseFloat(arr[i+1]);
    for (let j = 0; j < arr.length; j++)
    {
        if (j < i-1)
        {
            div.push(arr[j]);
        }
        else if (j == i)
        {
            div.push(inter);
        }
        else if (j > i+1)
        {
            div.push(arr[j]);
        }
    }
    return div;
}
function add(arr, i)
{
    let add = [];
    let inter = parseFloat(arr[i-1]) + parseFloat(arr[i+1]);
    for (let j = 0; j < arr.length; j++)
    {
        if (j < i-1)
        {
            add.push(arr[j]);
        }
        else if (j == i)
        {
            add.push(inter);
        }
        else if (j > i+1)
        {
            add.push(arr[j]);
        }
    }
    return add;
}
function sous(arr, i)
{
    let sous = [];
    let inter = parseFloat(arr[i-1]) - parseFloat(arr[i+1]);
    for (let j = 0; j < arr.length; j++)
    {
        if (j < i-1)
        {
            sous.push(arr[j]);
        }
        else if (j == i)
        {
            sous.push(inter);
        }
        else if (j > i+1)
        {
            sous.push(arr[j]);
        }
    }
    inter = null;
    return sous;
}
  }
};