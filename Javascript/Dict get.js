
Object.prototype.get = function (key, def=null){
    return this[key] || def
}
