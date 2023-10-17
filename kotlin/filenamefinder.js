function isSubstringPresent(mainString, subString) {
    return mainString.includes(subString);
}

// Example usage:
const mainString = "This is a sample string";
const subString = "example";
const result = isSubstringPresent(mainString, subString);
console.log(result); // false