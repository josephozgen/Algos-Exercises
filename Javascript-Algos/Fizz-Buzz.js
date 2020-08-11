const FizzBuzz = (arr) => {
    for (num in arr) {
        if (arr[num] % 15 === 0) {
          console.log(arr[num] + "\nfizz buzz")  
        } else if (arr[num] % 3 === 0) {
            console.log(arr[num] + "\nfizz")
        } else if (arr[num] % 5 === 0) {
            console.log(arr[num] + "\nbuzz")
        } else {
            console.log(arr[num])
        }
    }
}

const numbers = [1,23,4,5,4,545,45,25]
FizzBuzz(numbers)
