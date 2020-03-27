function calc(expr)
{
    // TODO: Your awesome code here
    expr = expr.split(' ');
    let res = []
    const op = {
        '+': function (x, y) {return x + y;},
        '-': function (x, y) {return x - y;},
        '*': function (x, y) {return x * y;},
        '/': function (x, y) {return x / y;},
    }

    for (let i = 0; i < expr.length; i++)
    {
        if (isNaN(expr[i]))
        {
            res.push(op[i]( parseFloat(res.pop), parseFloat(res.pop)));
        }
        else
        {
            res.push(expr[i]);
        }
    }
        
            return res;
}
    
console.log(calc("4 2 /"));