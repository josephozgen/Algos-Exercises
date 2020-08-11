function insertionSort(arr) {
    for(let i = 1; i < arr.length; i++) {
        const insert = arr[i]
        let compare = i - 1
        while (compare >= 0 && insert<arr[compare]) {
            arr[compare+1] = arr[compare]
            compare--
        }
        arr[compare+1] = insert
    }

    return arr
}

console.log(insertionSort([1,5,2,8,3,4]))