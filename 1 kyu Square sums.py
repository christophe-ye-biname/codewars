def square_sums(num):
    tab = [i for i in range(1, num + 1)]
    """
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
    """
    def anagram(string):
        output = []
        def traverse(string, perm = ''):
            seen = set()
            if !string:
                output.append(perm)
                for i in range(len(string)):
                    if string[i] not in seen:
                        seen.add(string[i])
                        traverse(string[0,i] + string[i+1], perm + string[i])
        traverse(string)
        return output
    return anagram('abc')

print(square_sums(15))