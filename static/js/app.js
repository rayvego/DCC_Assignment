const urlParams = new URLSearchParams(window.location.search);
const query = urlParams.get("query");
console.log("Search Query:", query);