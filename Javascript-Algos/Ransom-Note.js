const defaultDict = ransom => {
    const object = {}
    for (let key in ransom) {
        const letter = ransom[key]
        object[letter] = 0
    }
    return object
}

const collections = {
    defaultDict,
}

const canConstruct = (ransomNote, magazine) => {
    const magDict = collections.defaultDict(ransomNote);
    for (let key in magazine) {
        const letter = magazine[key]
        magDict[letter] += 1
    }
    for (let key in ransomNote) {
        const letter = ransomNote[key]
        magDict[letter] -= 1
        if (magDict[letter] < 0) {
            return false
        }
    }
    return true
}

console.log(canConstruct('cc','aaacccb'))