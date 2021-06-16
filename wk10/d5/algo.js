/* **********FOR ATTENDANCE******************
Work on the algorithm and write names of participants in the array "Devs" at the very bottom of page.
Post the code (with the array) to your team chat in MatterMost. It is okay if the solution isn't complete but show you are working on it.

*********** REMEMBER *******************
1. We do algos in the morning everyday as a habit or routine because it is like nutrition or going to the gym. A little bit everyday helps you in the longrun.
2. Imagine if after bootcamp, you want to get ready for your interviews and want to keep practicing algorithms. It would be harder to maintain a habit if you don't already have it.
3. Benefits of daily algorithms it helps you stay sharp and able to solve problems quicker and more creatively. You will get familiar with more complex strategies and come up with more than 1 way to solve a problem.
4. Benefit of sharing your solution at the end is practice speaking about code and thought process. 

************ YOU MAY.... ****************
Continue working on other Project or Assignment AFTER algo is completed and posted.
*/

/*
  Given an array of ailements (illnesses), and an array of medication objects that have a nested array of treatedSymptoms
  return the medication name(s) that treats the most given symptoms
*/

const medications = [
  {
    name: "Sulforaphane",
    treatableSymptoms: [
      "dementia",
      "alzheimer's",
      "cancer",
      "inflammation",
      "neuropathy",
    ],
  },
  {
    name: "Longvida Curcumin",
    treatableSymptoms: [
      "pain",
      "inflammation",
      "depression",
      "arthritis",
      "anxiety",
    ],
  },
  {
    name: "Hericium erinaceus",
    treatableSymptoms: ["anxiety", "cognitive decline", "depression"],
  },
  {
    name: "Nicotinamide mononucleotide",
    treatableSymptoms: [
      "ageing",
      "low NAD",
      "obesity",
      "mitochondrial myopathy",
      "diabetes",
    ],
  },
  {
    name: "PainAssassinator",
    treatableSymptoms: [
      "pain",
      "inflammation",
      "cramps",
      "headache",
      "toothache",
      "back pain",
      "fever",
    ],
  },
];

/*
  Input: ailments1, medications
  Output: ["PainAssassinator", "Longvida Curcumin"]
  */
const ailments1 = ["pain"];

/*
  Input: ailments2, medications
  Output: ["Longvida Curcumin"]
  */
const ailments2 = ["pain", "inflammation", "depression"];

/*
  Input: ailments3, medications
  Output: []
  */
const ailments3 = ["existential dread"];

// Time: O(n*m) where n is meds length and m is longest treatableSymptoms length
function getMeMyMeds(ailments, meds) {
  // code here
}


// ******************************
// const Devs = []