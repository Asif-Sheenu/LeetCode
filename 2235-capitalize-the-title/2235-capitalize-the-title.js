/**
 * @param {string} title
 * @return {string}
 */
var capitalizeTitle = function (title) {

let t =title.split(" ")
  .map((c) =>
    c.length > 2
      ? c[0].toUpperCase() + c.slice(1).toLowerCase()
      : c.toLowerCase()
  )
  .join(" ");    return t
};