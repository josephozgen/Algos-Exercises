function arrayPartition(arr, startIdx = 0, endIdx = arr.length - 1) {
    let pivotIdx = Math.floor(Math.random() * (endIdx + 1))
    let pivot = arr[pivotIdx]

    while(startIdx < endIdx) {
        while(arr[startIdx] < pivot) {
            startIdx++
        }

        while(arr[endIdx] > pivot) {
            endIdx--
        }

        if (startIdx < endIdx) {
            let temp = arr[startIdx]
            arr[startIdx] = arr[endIdx]
            arr[endIdx] = temp
        }
    }
    return startIdx
}

const arr = [1,2,4,8,5,6]
console.log("Pivot value: " + arrayPartition(arr))
console.log(arr)