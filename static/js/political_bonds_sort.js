document.addEventListener("DOMContentLoaded", function () {
  Tablesort.extend("int", function (item) {
    return parseInt(item, 10);
  });

  Tablesort.extend("string", function (item) {
    return item.toString();
  });

  document.addEventListener("tablesorter-initialized", function (event) {
    // Add event listeners for sort functionality
    var table = document.getElementById("bondsTable");
    var header = document.getElementById("table-header");

    header.addEventListener("click", function (e) {
      // Check if the target is a table header cell
      if (e.target.tagName === "TH") {
        var index = Array.prototype.indexOf.call(header.children, e.target);
        var sortType = e.target.getAttribute("data-sort");

        // Sort the table based on the clicked header cell
        table.sortTable(index, sortType);
      }
    });
  });
});
