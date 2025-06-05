Array.prototype.random = function () {
    return this[Math.floor((Math.random()*this.length))];
}
const colors = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"];

const target = document.getElementById("payload-target");
target.style.backgroundColor = colors.random();