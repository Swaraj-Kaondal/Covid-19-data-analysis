// URLS
export var localBaseUrl = "http://localhost:8000/";
// var baseURL = "https://ibmcovid1.herokuapp.com/";
//export var baseURL = "http://localhost:8000/";
export var baseURL = "https://26a972ce0870.ngrok.io/";
export var current_stats = baseURL + "India/";
export var all_states = baseURL + "statesTotal/";
export var state_wise = baseURL + "state/";
export var all_patients = baseURL + "allPatients/";
export var patient_filter = "patient/";

// Functions
// returns CARD of whole country wrt time
export async function getCurrentData(dataUrl) {
  const response = await fetch(dataUrl);
  const jsonData = await response.json();
  // console.log("jsonData is: " + jsonData.C);
  return jsonData;
}

//  convert normal array to chartJS suitable array
export function jsonify(value, index, array) {
  return { x: index, y: value };
}

// Styles
export const main_center = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};
