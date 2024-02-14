#!/usr/bin/node
const { dict } = require('./101-data');

function computeUserIdsByOccurrence(inputDict) {
  const resultDict = {};

  for (const userId in inputDict) {
    const occurrences = inputDict[userId];

    if (resultDict[occurrences]) {
      resultDict[occurrences].push(userId);
    } else {
      resultDict[occurrences] = [userId];
    }
  }

  return resultDict;
}

const newUserIdsByOccurrence = computeUserIdsByOccurrence(dict);
console.log(newUserIdsByOccurrence);