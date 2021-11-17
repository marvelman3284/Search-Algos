function sort(arr) {
  for(let i = 0; i < arr.length - 1; i++) {
    for (let j = 0; i < arr.length - j - 1; j++) {
      if (arr[j] > arr[j+1]) {
        let temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
      } 
    }
  }
  return arr;
}

function genArr(length, max) {
  let arr = [];
  for (let i = 0; i < length; i++) {
    arr.push(Math.floor(Math.random() * max));
  }
  return arr;
}

let arr = genArr(1000, 100000); 
console.log(sort(arr));
