function anagram(string){
  const output = [];
  function traverse(string, perm = ''){
    const seen = new Set();
    if (!string) output.push(perm)
    for (let i = 0; i < string.length; i++){
      if (!seen.has(string[i])){
        seen.add(string[i]);
        traverse(string.slice(0,i) + string.slice(i+1), perm + string[i]);
      }
    }
  }
  traverse(string)
  return output
}
let str = "abc";
console.log(anagram(str));