function selectionSort(arr) {
    for(let i=0; i<arr.length; i++) {
        let minIdx = i
        for(let j=i+1; j<arr.length; j++) {
            if(arr[minIdx] > arr[j]) {
                minIdx = j
            }
        }
        if(minIdx !== i) {
            let temp = arr[i]
            arr[i] = arr[minIdx]
            arr[minIdx] = temp
        }
    }
    return arr
}
console.log(selectionSort([1,5,2,8,3,4]))