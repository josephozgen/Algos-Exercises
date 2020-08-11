function combineSortedArrays(arr1, arr2) {
    let mergedArr = []
    let idx1 = 0
    let idx2 = 0
    let i = 0

    while(i<(arr1.length + arr2.length)) {
        if ((idx2 >= arr2.length) || (arr1[idx1] < arr2[idx2])) {
            mergedArr[i] = arr1[idx1]
            idx1++
        } else {
            mergedArr[i] = arr2[idx2]
            idx2++
        }
        i++
    }
    return mergedArr
}

console.log(combineSortedArrays([2,4,6],[1,3,5]))

function mergeSort(arr) {
    if (arr.length <= 1) return arr
    const sliceIndex = Math.floor(arr.length/2)
    const firstHalf = arr.slice(0, sliceIndex)
    const secondHalf = arr.slice(sliceIndex)
    return combineSortedArrays(mergeSort(firstHalf), mergeSort(secondHalf))
}

console.log(mergeSort([1,5,2,8,3,4]))