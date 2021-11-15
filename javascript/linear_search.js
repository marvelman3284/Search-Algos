function linear_search(arr, find_val) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == find_val) {
      return i
    }
  }
}

let genRandomList = (long) => {
  let arr = []; 
  for (let i = 0; i < long; i++) {
    let add = (Math.floor(Math.random() * 100 + 1))
    arr.push(add)
  }
  return arr 
}

let arr = genRandomList(10)
let find = arr[Math.floor(Math.random() * (arr.length + 1))]
console.log(find)
console.log(arr)
let search = linear_search(arr, find)

console.debug(search)
