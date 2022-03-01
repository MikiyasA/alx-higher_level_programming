#!/use/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOc = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      nOc += 1;
    }
  }
  return nOc;
};
