let object = { "a": { "b": { "c": "d" } } }
function getValue(obj, keys) {
  const keysArray = keys.split("/")
  if(keysArray.length < 1 ){
    return {}
  }
  let value = obj
  keysArray.map(i => {
    value = value?.[i]
  })
 return value
}
console.log(getValue(object, "a/b/c"))