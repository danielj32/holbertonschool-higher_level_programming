#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let ct = 0; ct < x; ct++) {
    theFunction();
  }
};
