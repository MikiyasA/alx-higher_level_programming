#!/usr/bin/node
exports.esrever = function (list) {
  let l = list.length - 1;
  for (let i = 0; i < l; i++) {
    const temp = list[l];
    list[l] = list[i];
    list[i] = temp;
    i++;
    l--;
  }
  return list;
};
