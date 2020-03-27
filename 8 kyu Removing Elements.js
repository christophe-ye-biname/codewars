function removeEveryOther(arr){
    return arr.filter((elem, i) => {
        return i % 2 === 0;
    })
    
}
console.log(removeEveryOther([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

//[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == [1, 3, 5, 7, 9]